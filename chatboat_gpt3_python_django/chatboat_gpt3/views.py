from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

def chatbot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        
        response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = user_input,
        #prompt = f"translate this text to marathi"
        temperature = 0.6,
        max_tokens = 150
        )
        chatbot_response = response.choices[0].text
        print(response.choices[0].text)
    return render(request, 'home.html', {"response": chatbot_response})