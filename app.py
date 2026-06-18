import os
from dotenv import load_dotenv
from google import genai

# 1. Load the secret key from your .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API Key missing! Check your .env file setup.")

# 2. Initialize the Gemini Client
client = genai.Client(api_key=api_key)

def start_chat():
    print("=============================================")
    print("Gemini Chatbot Live! Type 'exit' to stop.")
    print("=============================================")
    
    # 3. Create a continuous chat session (keeps memory)
    chat = client.chats.create(model="gemini-2.5-flash")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower().strip() == 'exit':
            print("Chat session closed.")
            break
            
        if not user_input.strip():
            continue
            
        # 4. Send message and print the response
        response = chat.send_message(user_input)
        print(f"\nBot: {response.text}")

if __name__ == "__main__":
    start_chat()
