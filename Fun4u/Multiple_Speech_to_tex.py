import speech_recognition as sr
from translation import google
r = sr.Recognizer()

with sr.Microphone() as scourse:
    print('Say Something')
    audio = r.listen(scourse)
    print('Done')

text = r.recognize_google(audio,language = 'hi-IN')

print(text)

print(r.recognize_google(audio))

print(google('hello world!', dst = 'hi-IN'))
