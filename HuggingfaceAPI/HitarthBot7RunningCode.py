from huggingface_hub import InferenceClient

client = InferenceClient(api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions.create(
    model="microsoft/DialoGPT-medium", 
	messages=messages, 
	max_tokens=500
)

print(completion.choices[0].message)
