"""Quick test: synthesize one sentence with a sherpa-onnx VITS model and print stats."""
import sys, wave
import numpy as np
import sherpa_onnx

model_dir, text, out = sys.argv[1], sys.argv[2], sys.argv[3]
speed = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
cfg = sherpa_onnx.OfflineTtsConfig(
    model=sherpa_onnx.OfflineTtsModelConfig(
        vits=sherpa_onnx.OfflineTtsVitsModelConfig(
            model=f"{model_dir}/model.onnx", tokens=f"{model_dir}/tokens.txt",
            noise_scale=0.667, noise_scale_w=0.8, length_scale=1.0),
        num_threads=2, provider="cpu"),
)
tts = sherpa_onnx.OfflineTts(cfg)
audio = tts.generate(text, sid=0, speed=speed)
s = np.array(audio.samples, dtype=np.float32)
print("sr", audio.sample_rate, "dur %.2fs" % (len(s) / audio.sample_rate), "peak %.3f" % np.abs(s).max(), "rms %.4f" % np.sqrt((s**2).mean()))
pcm = (np.clip(s, -1, 1) * 32767).astype(np.int16)
with wave.open(out, "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(audio.sample_rate); w.writeframes(pcm.tobytes())
