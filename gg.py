from googletrans import Translator

trans = Translator()

text = trans.translate("Hello", dest="fr", src="en")

print(text.text)