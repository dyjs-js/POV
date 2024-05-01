"""
import openai

# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"


# ChatGPT로 요약 함수
def summarize_with_chatgpt(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.5,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )
    return response.choices[0].text.strip()


# 예시 텍스트
example_text = 
Django는 파이썬으로 작성된 오픈 소스 웹 프레임워크입니다.
MTV(Model-Template-View) 패턴을 기반으로 한다.
장고의 주요 목표는 개발을 빠르고 쉽게 만들어주는 것입니다.


# ChatGPT를 사용하여 텍스트 요약
summary = summarize_with_chatgpt(example_text)
print("요약된 텍스트:", summary)
"""
