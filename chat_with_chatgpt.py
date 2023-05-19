import openai

# Make sure to replace 'YOUR_API_KEY' with your actual OpenAI API key. 
# You can obtain an API key by signing up for OpenAI's API access.
openai.api_key = 'YOUR_API_KEY'

def call_openai_api(prompt):
    # Define parameters for the API call
    model = 'gpt-3.5-turbo'
    max_tokens = 100

    # Call the OpenAI API
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Extract the generated message from the API response
    message = response.choices[0].text.strip()

    return message

# Example usage
user_prompt = "What is the capital of France?"
api_response = call_openai_api(user_prompt)
print(api_response)