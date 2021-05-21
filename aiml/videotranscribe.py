#list of modules required
#pip install Wave
#pip install moviepy
#pip install SpeechRecognition

import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip, VideoFileClip

input_video_path="C:/msrana/projects/pythonapps/sandbox/aiml/samplevideo3.mp4"
transcribed_audio_file_name = "C:/msrana/projects/pythonapps/sandbox/aiml/transcribed_speech.wav"
image_file_name = "C:/msrana/projects/pythonapps/sandbox/aiml/exported_image1.jpg"

video_clip=VideoFileClip(input_video_path)
video_clip.save_frame(image_file_name, t='00:00:10') # frame at time t=10sec

print("Image Export Complete")

audioclip = AudioFileClip(input_video_path)
audioclip.write_audiofile(transcribed_audio_file_name)

r = sr.Recognizer()
with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)

total_duration = math.ceil(duration / 60)

for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open("transcription.txt", "a")
    f.write(r.recognize_google(audio, language = "en-IN"))
    f.write(" ")
f.close()
print("Transcription Completed") 

