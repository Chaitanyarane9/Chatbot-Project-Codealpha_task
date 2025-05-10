import random
import nltk
import datetime
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "thanks": ["thanks", "thank you", "thx"],
    "help": ["help", "can you assist", "i need support"],
    "identity": ["who are you", "what is your name", "what are you"],
    "mood": ["how are you", "how are you doing", "what's up"],
    "time": ["what time is it", "tell me the time", "current time"],
    "date": ["what is the date", "today's date", "what day is it"]
}

responses = {
    "greeting": ["Hi there! 👋", "Hello!", "Hey! How can I help you today?"],
    "goodbye": ["Goodbye! 👋", "Take care!", "See you later!"],
    "thanks": ["You're welcome!", "No problem 😊", "Anytime!"],
    "help": ["I'm here to help! Ask me anything.", "What do you need help with?"],
    "identity": ["I'm your friendly chatbot 🤖", "I'm a virtual assistant created to chat with you!"],
    "mood": ["I'm doing great! How about you?", "Just chilling in cyberspace 😎"],
}

def preprocess(sentence):
    words = nltk.word_tokenize(sentence.lower())
    return [lemmatizer.lemmatize(w) for w in words]

def evaluate_math(expression):
    try:
        return str(eval(expression))
    except:
        return None

def get_bot_response(message):
    message = message.lower()

    # Try math evaluation first
    math_result = evaluate_math(message)
    if math_result:
        return f"The answer is: {math_result}"

    words = preprocess(message)

    # Time & date
    if any(phrase in message for phrase in intents["time"]):
        return f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}"

    if any(phrase in message for phrase in intents["date"]):
        return f"Today's date is {datetime.datetime.now().strftime('%A, %B %d, %Y')}"

    # Check other intent responses
    for intent, keywords in intents.items():
        if any(word in message for word in keywords):
            return random.choice(responses.get(intent, []))

    return random.choice([
        "I'm not sure I understand 🤔", 
        "Can you please rephrase that?", 
        "Tell me more about that."
    ])
