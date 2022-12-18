import math
import wave
import struct


def save_wav(file_name, audio, samplerate=44100.0):
    wav_file = wave.open(file_name, "w")
    wav_file.setparams(
        (1, 2, samplerate, len(audio), "NONE", "not compressed"))
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))
    wav_file.close()


def append_silence(audio, samplerate=44100.0, duration_milliseconds=500):
    for x in range(int(duration_milliseconds * (samplerate / 1000.0))):
        audio.append(0.0)
    return audio


def append_sinewave(audio, samplerate=44100.0, freq=150.0, duration_milliseconds=500, volume=1.0):
    for x in range(int(duration_milliseconds * (samplerate / 1000.0))):
        audio.append(volume * math.sin(2 * math.pi * freq * (x / samplerate)))
    return audio


def append_coswave(audio, samplerate=44100.0, freq=150.0, duration_milliseconds=500, volume=1.0):
    for x in range(int(duration_milliseconds * (samplerate / 1000.0))):
        # (-32768) <= number <= 32767
        audio.append(volume * math.cos(2 * math.pi * freq * (x / samplerate)))
    return audio


def append_squarewave(audio, samplerate=44100.0, freq=150.0, duration_milliseconds=500, volume=1.0):
    for x in range(int(duration_milliseconds * (samplerate / 1000.0))):
        audio.append(volume * ((2 * math.pi * freq * ((int(duration_milliseconds *
                     (samplerate / 1000.0))) / samplerate))/1000))  # (-32768) <= number <= 32767
    return audio
