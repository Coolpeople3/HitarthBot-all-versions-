import tkinter as tk
import requests
import base64

# Encoded API key (replace with your actual key encoded in base64)
encoded_api_key = "aGZfTmNJQ3dUaGllQVpHYnJqdldKeWptWGh2cEphUUZMQk5Oag=="

# Decode API key at runtime
API_KEY = base64.b64decode(encoded_api_key).decode("utf-8")

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# Function to get bot response
def get_bot_response():
    user_input = user_entry.get()
    if user_input.lower() == "exit":
        root.quit()

    payload = {"inputs": user_input}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            result = response.json()
            if result and isinstance(result, list):
                bot_response = result[0].get("generated_text", "No response.")
                bot_output_label.config(text=f"Bot: {bot_response}")
            else:
                bot_output_label.config(text="Bot: No valid response received.")
        except Exception as e:
            bot_output_label.config(text=f"Bot: Error processing response: {e}")
    elif response.status_code == 503:
        bot_output_label.config(text="Bot: Model is loading. Please wait and try again.")
    else:
        bot_output_label.config(text=f"Error {response.status_code}: {response.text}")

# Create main tkinter window
root = tk.Tk()
root.title("Chatbot GUI")

# User input section
user_label = tk.Label(root, text="You:")
user_label.pack()

user_entry = tk.Entry(root, width=50)
user_entry.pack()

send_button = tk.Button(root, text="Send", command=get_bot_response)
send_button.pack()

# Bot response section
bot_output_label = tk.Label(root, text="Bot: ", wraplength=400)
bot_output_label.pack()

# Run the tkinter main loop
root.mainloop()
