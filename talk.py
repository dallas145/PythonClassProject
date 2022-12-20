import time
from gtts import gTTS
from pygame import mixer
import tempfile

def talk(sentence, lang):
    with tempfile.NamedTemporaryFile(delete=True) as f:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(f.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(f.name))
        mixer.music.play(loops=0)

if __name__ == "__main__":
    talk('大家好!','zh-tw')
    time.sleep(3)