import os
from gtts import gTTS
import googletrans

if __name__ == '__main__':
    translator = googletrans.Translator()
    text = input('Enter the text')
    lang = input('Enter the language').lower()
    if lang in googletrans.LANGCODES:
        myobj=gTTS(text=translator.translate(text=text,dest=googletrans.LANGCODES[lang]).text,lang=googletrans.LANGCODES[lang],slow=False,)
        myobj.save('texttospeech.mp3')
        os.system('start texttospeech.mp3')
    else:
        print('Toh bhi upar error aayega')
