# Import the necessary libraries
import random

# Define a list of responses
responses = [
    "Hello!",
    "How are you?",
    "What can I do for you?",
    "I'm sorry, I didn't understand your question.",
    "Can you please elaborate on that?",
    "I see. Let me think about that for a moment.",
    "Can you provide more information?",
]

# Define a function that generates a response to a user's input
def generate_response(input_message):
    # Choose a random response from the list
    response = random.choice(responses)
    return response

# Define a function that runs the chatbot
def run_chatbot():
    # Prompt the user for input
    user_input = input("User: ")

    # Generate a response
    response = generate_response(user_input)

    # Print the response
    print("Chatbot: " + response)

    # Run the chatbot again until the user types "exit"
    if user_input.lower() != "exit":
        run_chatbot()

# Start the chatbot
run_chatbot()