import nltk
import json
import random
from nltk.corpus import stopwords
#from spellchecker import SpellChecker


with open(r"C:\TK\responses.json", encoding='utf-8') as file:
    intents = json.load(file)

# Initialize spellchecker
#spell = SpellChecker()

# Preprocess intents for spellchecking
for intent in intents['intents']:
    for pattern in intent['patterns']:
        tokens = nltk.word_tokenize(pattern)
        filtered_tokens = [word.lower() for word in tokens if word.lower() not in stopwords.words('english')]
        intent['filtered_patterns'] = filtered_tokens


def get_intent(user_input, intents):
    matched_intents = []
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                matched_intents.append(intent)
                break  # Break out of inner loop after finding a match
    return matched_intents


def chatbot_response(user_input, intents):
    matched_intents = get_intent(user_input, intents)

    if matched_intents:
        intent = random.choice(matched_intents)
        response = random.choice(intent['responses'])
        # Remove extra spaces
        response = ' '.join(response.split())
        return response
    else:
        return "I'm sorry, I didn't understand that."


def main():
    #intents = load_intents(r"C:\Minee Pro-eject\responses.json")

    print("Welcome! I'm Camila a simple chatbot. You can start chatting with me. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Camila: Goodbye! Take care!")
            break
        else:
            response = chatbot_response(user_input, intents)
            print("Camila:", response)


if __name__ == "__main__":
    main()
