"""Transcribe each narration WAV with Whisper (sherpa-onnx) and compare to the script.

Usage: python3 verify_narration.py <whisper_dir> <narration.json> <audio_dir>
Prints per-slide word error rate (WER) and the transcript.
"""
import json
import re
import sys
import wave
from pathlib import Path

import numpy as np
import sherpa_onnx


def read_wav(path: Path):
    with wave.open(str(path)) as w:
        sr = w.getframerate()
        data = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
    return sr, data.astype(np.float32) / 32768.0


def words(text: str):
    return re.findall(r"[a-zčćđšž]+", text.lower())


def wer(ref, hyp) -> float:
    d = np.zeros((len(ref) + 1, len(hyp) + 1), dtype=int)
    d[:, 0] = range(len(ref) + 1)
    d[0, :] = range(len(hyp) + 1)
    for i in range(1, len(ref) + 1):
        for j in range(1, len(hyp) + 1):
            cost = 0 if ref[i - 1] == hyp[j - 1] else 1
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + cost)
    return d[len(ref), len(hyp)] / max(1, len(ref))


def load_recognizer(wdir: str) -> sherpa_onnx.OfflineRecognizer:
    # Whisper has no Serbian-specific Latin model; Croatian decodes Serbian Latin well.
    return sherpa_onnx.OfflineRecognizer.from_whisper(
        encoder=f"{wdir}/turbo-encoder.int8.onnx",
        decoder=f"{wdir}/turbo-decoder.int8.onnx",
        tokens=f"{wdir}/turbo-tokens.txt",
        language="hr",
        task="transcribe",
        num_threads=4,
    )


def transcribe(rec: sherpa_onnx.OfflineRecognizer, sr: int, samples: np.ndarray) -> str:
    stream = rec.create_stream()
    stream.accept_waveform(sr, samples)
    rec.decode_stream(stream)
    return stream.result.text.strip()


def main() -> None:
    wdir, narration_path, audio_dir = sys.argv[1], sys.argv[2], Path(sys.argv[3])
    rec = load_recognizer(wdir)
    slides = json.loads(Path(narration_path).read_text(encoding="utf-8"))
    total_err, total_words = 0.0, 0
    for item in slides:
        sr, samples = read_wav(audio_dir / f"slide-{item['slide']:02d}.wav")
        hyp = transcribe(rec, sr, samples)
        ref_words, hyp_words = words(item.get("tts", item["text"])), words(hyp)
        e = wer(ref_words, hyp_words)
        total_err += e * len(ref_words)
        total_words += len(ref_words)
        print(f"{item['slide']:2d}  WER {e:4.0%}  | {hyp}")
    print(f"overall WER {total_err / total_words:.1%} over {total_words} words")


if __name__ == "__main__":
    main()
