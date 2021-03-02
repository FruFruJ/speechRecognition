import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()
gg=sr.AudioFile('dall.aiff')
with gg as source:
    r.adjust_for_ambient_noise(source)
    audio=r.record(source)
print(type(audio))
print(r.recognize_google(audio))

mc = sr.Microphone(device_index=1)
with mc as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    l = r.recognize_google(audio, show_all=True, language='it-IT')
    print(l)
    print("Possible transcriptions:")
    if (l != []):
        for prediction in l['alternative']:
            print(" " + prediction["transcript"] + " (" + str(prediction["confidence"] * 100) + "%)")
except LookupError:  # speech is unintelligible
    print("Could not understand audio")


