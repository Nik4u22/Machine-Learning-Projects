import openai

def askGPT(text):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150
    )
    return print(response.choices[0].text)

def main():
    while True:
        print('GPT: Ask me a question\n')
        myQn = input()
        askGPT(myQn)
        print('\n')

main()
