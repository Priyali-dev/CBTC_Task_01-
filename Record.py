import sounddevice as sd
import wavio

# Set the audio parameters
sample_rate = 44100
channels = 2

# Set the recording duration (in seconds)
duration = 10

# Record audio
print("Recording audio...")
myrecording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
sd.wait()

# Save the recorded audio to a WAV file
filename = "recorded_audio.wav"
wavio.write(filename, myrecording, sample_rate, sampwidth=2)

print(f"Audio recorded and saved to {filename}")
