import tkinter as tk
from tkinter import scrolledtext
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")
# Replace with your Hugging Face API Key
API_KEY = api_key

# Initialize Hugging Face Inference Client
client = InferenceClient(api_key=API_KEY)

# Function to handle sending messages
def send_message():
    user_message = user_input.get().strip()
    if not user_message:
        return  # Ignore empty messages

    # Display the user's message
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_message}\n")
    chat_window.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)  # Clear input box

    # Prepare the prompt for the bot
    prompt = (
        "You are HitarthBot, a helpful and friendly chatbot.\n"
        f"You: {user_message}\nBot:"
    )

    try:
        # Call the Hugging Face API
        response = client.text_generation(
            model="openassistant/oasst-sft-4-pythia-12b-epoch-3.5",  # Public model
            prompt=prompt,
            max_new_tokens=150,
            temperature=0.8,
        )
        bot_response = response.strip()  # Clean the response text

        # Display the bot's response
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"Bot: {bot_response}\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)  # Auto-scroll to the bottom
    except Exception as e:
        # Display error messages
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"Error: {str(e)}\n")
        chat_window.config(state=tk.DISABLED)

# Create the main GUI window
root = tk.Tk()
root.title("HitarthBot")
root.geometry("500x600")
root.resizable(False, False)

# Create the chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create the user input field
user_input = tk.Entry(root, font=("Arial", 14))
user_input.pack(pady=5, padx=10, fill=tk.X)

# Create the send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# Allow pressing Enter to send messages
def enter_pressed(event):
    send_message()

root.bind("<Return>", enter_pressed)

# Start the main event loop
root.mainloop()
