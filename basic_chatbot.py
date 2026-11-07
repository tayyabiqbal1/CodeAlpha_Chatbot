"""Basic Rule-Based Chatbot
The bot matches keywords in the user's message to predefined replies.
Concepts: dictionary, loops, string methods, input/output.
"""

import random
import string

BOT_NAME = "Chatty"

# Each rule: a tuple of trigger phrases -> a list of possible replies
RULES = [
    (("hello", "hi", "hey"),
     ["Hello! How can I help you?", "Hi there! Nice to see you.", "Hey! What's up?"]),
    (("how are you", "how r u"),
     ["I'm doing great, thanks for asking! How about you?",
      "I'm just a bunch of code, but I'm feeling good!"]),
    (("your name", "who are you"),
     [f"I'm {BOT_NAME}, a simple rule-based chatbot."]),
    (("fine", "good", "great"),
     ["Glad to hear that!"]),
    (("help",),
     ["Try saying hello, asking how I am, asking my name, or saying bye."]),
    (("thank", "thanks"),
     ["You're welcome!", "Happy to help!"]),
]

EXIT_WORDS = ("bye", "goodbye", "exit", "quit")

DEFAULT_REPLIES = [
    "Sorry, I didn't understand that. Type 'help' to see what I can do.",
    "Hmm, I don't know how to answer that yet.",
]


def clean(text):
    """Lowercase the text and remove punctuation so matching is easier."""
    text = text.lower().strip()
    return text.translate(str.maketrans("", "", string.punctuation))


def matches(trigger, words, message):
    """A one-word trigger must match a whole word ('hi' won't match 'this').
    A multi-word trigger can appear anywhere in the message."""
    if " " in trigger:
        return trigger in message
    return any(w.startswith(trigger) if trigger in ("thank",) else w == trigger
               for w in words)


def get_reply(user_input):
    message = clean(user_input)
    words = message.split()

    for triggers, replies in RULES:
        for trigger in triggers:
            if matches(trigger, words, message):
                return random.choice(replies)

    return random.choice(DEFAULT_REPLIES)


def main():
    print(f"{BOT_NAME}: Hi! I'm {BOT_NAME}. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            print(f"{BOT_NAME}: Say something!")
            continue

        if any(w in clean(user_input).split() for w in EXIT_WORDS):
            print(f"{BOT_NAME}: Goodbye! Have a great day!")
            break

        print(f"{BOT_NAME}: {get_reply(user_input)}")


if __name__ == "__main__":
    main()