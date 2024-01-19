import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "How can I help you today?"]],
    ["how are you", ["I'm good, thank you!", "I'm doing well, how about you?"]],
    ["(what is your name|who are you)", ["I'm a simple chatbot.", "You can call me ChatBot."]],
    ["bye|goodbye", ["Goodbye!", "Have a great day!"]],
    ["(thanks|thank you)", ["You're welcome!", "No problem!"]],
    ["default", ["I'm not sure how to respond to that."]],
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Function to start the conversation
def chat_with_user():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    # Download necessary resources for nltk if not already present
    nltk.download('punkt')

    # Start the conversation
    chat_with_user()
