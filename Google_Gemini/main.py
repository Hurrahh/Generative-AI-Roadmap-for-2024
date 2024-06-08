# pip install google-generativeai
import google.generativeai as genai

# To get your api key
# Visit: https://aistudio.google.com/app/apikey

# Configure api key
genai.configure(api_key="Your api key")

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is Generative AI")

print(response.text)

'''
Check out https://ai.google.dev/gemini-api/docs/models/gemini 
Try different model with their uses
"gemini-1.5-pro" -- for complex task like code generation, text generation/editing,etc
"gemini-1.5-flash" -- fast performance for normal question answering response
"gemini-pro-vision" -- generating image descriptions or identifying objects in images
'''

