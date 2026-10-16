"""Synthesize per-slide Serbian narration with a sherpa-onnx VITS voice.

Every slide gets exactly SLIDE_SECONDS of audio: a short lead-in, the speech,
then silence. If the speech is too long at normal speed it is sped up a little
(at most the last of SPEEDS); slides that still do not fit are reported.

With WHISPER_DIR set, each slide is synthesized TAKES times (the voice varies
from take to take), every take is transcribed with Whisper, and the take with
the lowest word error rate is kept, the way one picks the best take in a
recording session.

Usage: python3 make_narration.py <model_dir> <narration.json> <out_dir>
Environment: TRANSLIT=sl|cs|sk, WHISPER_DIR=<dir>, TAKES=<n>, SLIDES=3,17 (redo only these)
"""
import json
import os
import sys
import wave
from pathlib import Path

import numpy as np
import sherpa_onnx

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translit import to_czech, to_slovak, to_slovenian  # noqa: E402
from verify_narration import load_recognizer, transcribe, wer, words  # noqa: E402

TRANSLIT = {"": lambda t: t, "sl": to_slovenian, "cs": to_czech, "sk": to_slovak}

SLIDE_SECONDS = 5.0
LEAD_IN = 0.25
MAX_SPEECH = SLIDE_SECONDS - LEAD_IN - 0.25
SPEEDS = (1.0, 1.04, 1.08, 1.12)


def load_tts(model_dir: str) -> sherpa_onnx.OfflineTts:
    cfg = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                model=f"{model_dir}/model.onnx",
                tokens=f"{model_dir}/tokens.txt",
                # Piper voices phonemize with espeak-ng; Coqui grapheme voices do not.
                data_dir=f"{model_dir}/espeak-ng-data" if os.path.isdir(f"{model_dir}/espeak-ng-data") else "",
                noise_scale=float(os.environ.get("NOISE_SCALE", "0.667")),
                noise_scale_w=float(os.environ.get("NOISE_SCALE_W", "0.8")),
                length_scale=1.0,
            ),
            num_threads=4,
            provider="cpu",
        ),
    )
    return sherpa_onnx.OfflineTts(cfg)


def trim_silence(samples: np.ndarray, sr: int, threshold: float = 0.002) -> np.ndarray:
    """Cut leading and trailing near-silence so padding is under our control."""
    loud = np.where(np.abs(samples) > threshold)[0]
    if loud.size == 0:
        return samples
    pad = int(0.15 * sr)
    return samples[max(0, loud[0] - pad): loud[-1] + pad]


def synthesize(tts: sherpa_onnx.OfflineTts, text: str):
    """Return the trimmed speech at the slowest speed that fits MAX_SPEECH."""
    for speed in SPEEDS:
        audio = tts.generate(text, sid=0, speed=speed)
        sr = audio.sample_rate
        speech = trim_silence(np.asarray(audio.samples, dtype=np.float32), sr)
        if len(speech) / sr <= MAX_SPEECH:
            break
    return speech, sr, speed


def place_on_slide(speech: np.ndarray, sr: int) -> np.ndarray:
    """Normalize the peak and put the speech LEAD_IN into a SLIDE_SECONDS buffer."""
    speech = speech * (0.89 / (float(np.abs(speech).max()) or 1.0))
    total, lead = int(SLIDE_SECONDS * sr), int(LEAD_IN * sr)
    slide_audio = np.zeros(total, dtype=np.float32)
    end = min(total, lead + len(speech))
    slide_audio[lead:end] = speech[: end - lead]
    return slide_audio


def write_wav(path: Path, samples: np.ndarray, sr: int) -> None:
    pcm = (np.clip(samples, -1.0, 1.0) * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())


def main() -> None:
    model_dir, narration_path, out_dir = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    out_dir.mkdir(parents=True, exist_ok=True)
    slides = json.loads(Path(narration_path).read_text(encoding="utf-8"))
    only = {int(s) for s in os.environ.get("SLIDES", "").split(",") if s.strip()}
    translit = TRANSLIT[os.environ.get("TRANSLIT", "")]
    tts = load_tts(model_dir)
    rec = load_recognizer(os.environ["WHISPER_DIR"]) if os.environ.get("WHISPER_DIR") else None
    takes = int(os.environ.get("TAKES", "5")) if rec else 1
    report_path = out_dir / "report.json"
    report = {}
    if only and report_path.exists():
        report = {r["slide"]: r for r in json.loads(report_path.read_text(encoding="utf-8"))}
    for item in slides:
        if only and item["slide"] not in only:
            continue
        ref = item.get("tts", item["text"])
        best = None
        for _ in range(takes):
            speech, sr, speed = synthesize(tts, translit(ref))
            speech_s = len(speech) / sr
            slide_audio = place_on_slide(speech, sr)
            hyp = transcribe(rec, sr, slide_audio) if rec else ""
            err = wer(words(ref), words(hyp)) if rec else 0.0
            # Prefer takes that fit, then fewer recognition errors, then less speed-up.
            key = (speech_s > MAX_SPEECH, err, speed)
            if best is None or key < best["key"]:
                best = {"key": key, "audio": slide_audio, "sr": sr, "speed": speed,
                        "speech_s": speech_s, "hyp": hyp, "err": err}
        name = f"slide-{item['slide']:02d}.wav"
        write_wav(out_dir / name, best["audio"], best["sr"])
        fits = best["speech_s"] <= MAX_SPEECH
        report[item["slide"]] = {"slide": item["slide"], "file": name, "speed": best["speed"],
                                 "speech_seconds": round(best["speech_s"], 2), "fits": fits,
                                 "wer": round(best["err"], 2), "transcript": best["hyp"]}
        print(f"slide {item['slide']:2d}  speed {best['speed']:.2f}  speech {best['speech_s']:4.2f}s  "
              f"{'ok' if fits else 'TOO LONG'}  WER {best['err']:4.0%}  | {best['hyp']}", flush=True)
    rows = [report[k] for k in sorted(report)]
    report_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    if rec:
        words_total = sum(len(words(s.get("tts", s["text"]))) for s in slides if s["slide"] in report)
        errs = sum(report[s["slide"]]["wer"] * len(words(s.get("tts", s["text"]))) for s in slides if s["slide"] in report)
        print(f"overall WER {errs / max(1, words_total):.1%} over {words_total} words")


if __name__ == "__main__":
    main()
