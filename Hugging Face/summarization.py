import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import pipeline

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"]=os.getenv('HF_Token')


tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

pipe = pipeline("summarization", model=model,tokenizer=tokenizer)

llm= HuggingFacePipeline(pipeline=pipe)

text="Generative AI is a type of artificial intelligence (AI) that creates new content by learning patterns from existing data. It can generate text, images, music, and even video content that is similar to, but not identical to, the data it was trained on.\n\nGenerative AI works by using a process called generative modeling. This involves training a machine learning model on a large dataset, such as a collection of images, texts, or other data. The model learns the underlying patterns and structures in the data, and can then use these patterns to generate new content.\n\nThere are several types of generative AI models, including:\n\n1. Generative adversarial networks (GANs): These are a type of neural network that consist of two parts: a generator and a discriminator. The generator creates new content, while the discriminator tries to determine whether the content was created by the generator or was taken from the training data. The two parts are trained together, with the generator trying to improve its ability to create realistic content, and the discriminator trying to become better at identifying fake content.\n2. Variational autoencoders (VAEs)"

response = llm.invoke(text)
print(response)