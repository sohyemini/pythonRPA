from googletrans import Translator

# Create a translator object
translator = Translator()

#1. Text to be translated
text = "Hello, how are you?"
# Translate from English to Traditional Chinese
translated = translator.translate(text, src='en', dest='zh-tw')
# Print the original and translated text
print(f"Original1: {text}")
print(f"Translated1: {translated.text}")

#2 Text2 to be translated
text2 = "Welcome to Robotic Process Automation world!"
# Translate from English to Traditional Chinese
translated = translator.translate(text2, src='en', dest='zh-tw')
# Print the original and translated text
print(f"Original2: {text2}")
print(f"Translated2: {translated.text}")

#3 Text to be translated
text3 = "We can translate English to Chinese"
# Translate from English to Traditional Chinese
translated = translator.translate(text3, src='en', dest='zh-tw')
# Print the original and translated text
print(f"Original3: {text3}")
print(f"Translated3: {translated.text}")