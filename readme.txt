OpenAI offers an application programming interface (API) which is basically a gateway that allows you to leverage the power of GPT-3 to create a wide range of applications including:

text completion (generate and edit text);
image generation (image generation);
embeddings (search, classify and compare text); and
code completion (generate, edit and explain code).

GPT-3 (and natural language processing in general)
GPT stands for Generative Pretrained transformer and GPT 3.0 drives ChaGPT website. GPT is a fancy word for model to generate content.
1. Generative - generate content (nlp)
2. Pretrained - trained on data (Already trained on whole data available on Internet)
3. Transformer - Model

GPT is tarined using nlp based reinforcement learning techniques.
Transformer do encoding and decoding of text input given by user, In this process it breaks down the text into smallest sentence possible.
a) Encoding: How do i start learning to code? -> How learn code? and give weightage to each word.
b) Decoding: Evaluate context and predict best sequence of words as response
    Self affinationcode->How->Learn

Steps to follow

1. Register with OpenAI and generate secret API Key
2. Create simple python project using conda env
3. pip3 install openai
4. pip install python-dotenv 
Python-dotenv reads key-value pairs from a .env file and can set them as environment variables.
5. main.py - write code and run

We can also use streamlit, Django, Flask or Flutter to design UI