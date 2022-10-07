import googletrans
from googletrans import Translator

ndict = googletrans.LANGUAGES
text1 = "안녕하세요"

translator = Translator()
print(translator.detect(text1))

for i in ndict:
    trans1 = translator.translate(text1, src='ko', dest=i)
    print(f"{ndict[i]} 의 인사말 ", trans1.text)
