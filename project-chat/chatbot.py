import json
import random
import time

# Load keywords and responses from JSON file...
with open('responses.json', 'r') as file:
    config = json.load(file)

keywords = config["keywords"]
random_responses = config["random_responses"]

# Function to generate a random agent name....
def generate_agent_name():
    names = ["Manish", "Shivraj", "Aryan", "Batsal", "Rachit"]
    return random.choice(names)

# Logging function...
def log_session(user_name, log_data):
    with open(f"{user_name}_chat_log.txt", "w") as log_file:
        for entry in log_data:
            log_file.write(entry + "\n")

# Main chatbot function...
def chatbot():
    print("Welcome to The British College  Chatbot!")
    user_name = input("Please enter your name: ")
    agent_name = generate_agent_name()
    print(f"Hello {user_name}, I'm {agent_name}, your virtual assistant. Type 'bye' to exit.")
    
    chat_log = []
    while True:
        user_input = input(f"{user_name}: ").lower()
        chat_log.append(f"User: {user_input}")
        
        # Check for exit condition....
        if user_input in ["bye", "exit", "quit"]:
            print(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            chat_log.append(f"{agent_name}: Goodbye, {user_name}! Have a great day!")
            break
        
        # Simulate random disconnection....
        if random.random() < 0.05:  # 5% chance
            print(f"{agent_name}: Oops! It seems I've been disconnected. Please try again later.")
            chat_log.append(f"{agent_name}: Oops! It seems I've been disconnected. Please try again later.")
            break
        
        # Respond based on keywords or randomly
        response = None
        for keyword, reply in keywords.items():
            if keyword in user_input:
                response = reply
                break
        
        if not response:
            response = random.choice(random_responses)
        
        print(f"{agent_name}: {response}")
        chat_log.append(f"{agent_name}: {response}")
        time.sleep(random.uniform(0.5, 1.5))  # Add delay for realism
    
    # Save chat log
    log_session(user_name, chat_log)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
