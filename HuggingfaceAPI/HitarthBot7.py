import tkinter as tk
from tkinter import scrolledtext
from huggingface_hub import InferenceClient

# Replace with your Hugging Face API key
API_KEY = "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"

# Initialize the Hugging Face client
client = InferenceClient(api_key=API_KEY)

# Function to handle user input and get bot response
def send_message():
    user_message = user_input.get()
    if not user_message.strip():
        return  # Ignore empty messages

    # Display the user's message
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_message}\n")
    chat_window.config(state=tk.DISABLED)

    user_input.delete(0, tk.END)  # Clear the input box

    # Get the bot's response
    try:
        messages = [{"role": "user", "content": user_message}]
        completion = client.chat.completions.create(
            model="microsoft/DialoGPT-medium",
            messages=messages,
            max_tokens=500,
        )
        bot_response = completion.choices[0].message

        # Display the bot's response
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"Bot: {bot_response}\n")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)  # Auto-scroll to the bottom
    except Exception as e:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, f"Error: {str(e)}\n")
        chat_window.config(state=tk.DISABLED)

# Create the main GUI window
root = tk.Tk()
root.title("HitarthBot7")
root.geometry("500x600")
root.resizable(False, False)

# Create a chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create an input field
user_input = tk.Entry(root, font=("Arial", 14))
user_input.pack(pady=5, padx=10, fill=tk.X)

# Create a send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(pady=5)

# Allow pressing Enter to send messages
def enter_pressed(event):
    send_message()

root.bind("<Return>", enter_pressed)

# Start the main event loop
root.mainloop()
