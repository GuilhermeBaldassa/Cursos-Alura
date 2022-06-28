from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'
language = 'pt-br'

sp = gTTS(
    text='Batatinha quando nascem esparrama pelo chão, a livinha quando dorme põe a mão no coração. Vovô peidorrero',
    lang=language
)

sp.save(audio)
playsound(audio)