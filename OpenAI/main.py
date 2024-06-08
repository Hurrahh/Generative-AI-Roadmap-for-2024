from openai import OpenAI


# -- Get your api key here https://platform.openai.com/api-keys


client = OpenAI(openai_api_key = "your api_key",temperature=0.3)

## first way simple generate response
prompt = 'How can I make tea'

response = client.predict(prompt)

print(response.strip())


##-- Another way you can define role of system and user what you want with the LLM model

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message.content)
