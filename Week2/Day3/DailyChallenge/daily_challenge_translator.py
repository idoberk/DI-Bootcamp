# What You will learn :
# Modules

# Instructions :
# Consider this list

# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.

from deep_translator import GoogleTranslator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translated_words = {}

for word in french_words:
    translated_words[word] = GoogleTranslator(source="fr", target="en").translate(
        text=word
    )

print(translated_words)
