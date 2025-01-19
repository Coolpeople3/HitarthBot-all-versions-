import requests
import base64

encoded_api_key = "aGZfTmNJQ3dUaGllQVpHYnJqdldKeWptWGh2cEphUUZMQk5Oag=="  

API_KEY = base64.b64decode(encoded_api_key).decode("utf-8")

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        payload = {"inputs": user_input}
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            try:
                result = response.json()
                if result and isinstance(result, list):
                    bot_response = result[0].get("generated_text", "No response.")
                    print("HitarthBot:", bot_response)
                else:
                    print("HitarthBot: No valid response received.")
            except Exception as e:
                print("Bot: Error processing response:", e)
        elif response.status_code == 503:
            print("Bot: Model is loading. Please wait and try again.")
        else:
            print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    main()
