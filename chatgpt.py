import openai

# 발급받은 OpenAI API Key 기입
YOUR_API_KEY = '<your-openai-api-key>'


def ChatGPT(prompt, API_KEY=YOUR_API_KEY):
    # api key 세팅
    openai.api_key = API_KEY

    # ChatGPT API 호출 및 최신 언어 모델인 text-davinci-003을 가져옴
    completion = openai.Completion.create(
        engine='text-davinci-003'  # 'text-curie-001'  # 'text-babbage-001' #'text-ada-001'
        , prompt=prompt
        , temperature=0.5
        , max_tokens=1024
        , top_p=1
        , frequency_penalty=0
        , presence_penalty=0)

    return completion['choices'][0]['text']


def main():
    # 지문 입력 란
    prompt = input("Insert a prompt: ")
    print(ChatGPT(prompt).strip())


if __name__ == '__main__':
    main()
