import googletrans

def main(text):
    translator = googletrans.Translator()
    lang = input('Enter the language').lower()
    if lang in googletrans.LANGCODES:
        print(translator.translate(text=text,dest=googletrans.LANGCODES[lang]).text)
    else:
        print('Incorrect language')
        print(*[x for x in googletrans.LANGCODES],sep='\n')
        print('Try using any languages from these')


if __name__ == '__main__':
    text = input('Enter the text')
    main(text)
