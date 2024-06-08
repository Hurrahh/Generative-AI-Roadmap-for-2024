import openai

openai.api_key = "your api_key"

# -- Get your api key here https://platform.openai.com/api-keys
response = openai.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

print(response.data[0].url)

