from googletrans import Translator

# Create a translator object
translator = Translator()

def myTrans(txt):
    translated = translator.translate(txt, src='en', dest='zh-tw')
    print(f"Original1: {txt}")
    print(f"Translated1: {translated.text}")

#1. Text to be translated
text = "Hello, how are you?"
myTrans(text)

#2 Text2 to be translated
text2 = "Welcome to Robotic Process Automation world!"
myTrans(text2)

#3 Text to be translated
text3 = "We can translate English to Chinese"
myTrans(text3)