from googletrans import Translator

# Create a translator object
translator = Translator()

# Text to be translated
text = "Hello, how are you?"

# Translate from English to Traditional Chinese
translated = translator.translate(text, src='en', dest='zh-tw')

# Print the original and translated text
print(f"Original: {text}")
print(f"Translated: {translated.text}")
