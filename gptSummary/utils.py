# OpenAI API 키 설정
import os
from pathlib import Path
from openai import OpenAI
import environ

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
api_key = env("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)
"""
user_message = {
    "role": "user",
    "content": "타이타닉은 1997년에 개봉한 미국의 로맨스/재난 영화로, 제임스 카메론 감독의 작품이다. 영화는 실제로 발생한 1912년 타이타닉호 침몰 사건을 바탕으로 하고 있으며, 여성 주인공 로즈와 남성 주인공 잭의 사랑 이야기를 중심으로 전개된다. 이 영화는 역사적 사건을 배경으로 하면서도 로맨스와 스릴러적인 요소를 풍미하며 관객들에게 강한 여운을 남기는데, 특히 타이타닉호의 침몰 장면은 화려한 시각 효과와 함께 매우 인상적이다.",
}

# 시스템 메시지
assistant_message = {
    "role": "assistant",
    "content": "user_message 의 영화 내용을 요약합니다.",
}
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[user_message, assistant_message],
)
# 대화 결과 출력
# print(chat_completion.choices[0].message.content)
print(chat_completion.choices[0].message.content)
# print(dict(chat_completion).get("usage"))
# print(chat_completion.model_dump_json(indent=2))
"""

from openai import OpenAI


img_gt = client.images.generate(
    model="dall-e-3",
    prompt="타이타닉,영화,이타닉은 1997년에 개봉한 미국의 로맨스/재난 영화로, 제임스 카메론 감독의 작품이다. 영화는 실제로 발생한 1912년 타이타닉호 침몰 사건을 바탕으로 하고 있으며, 여성 주인공 로즈와 남성 주인공 잭의 사랑 이야기를 중심으로 전개된다. 이 영화는 역사적 사건을 배경으로 하면서도 로맨스와 스릴러적인 요소를 풍미하며 관객들에게 강한 여운을 남기는데, 특히 타이타닉호의 침몰 장면은 화려한 시각 효과와 함께 매우 인상적이다.슬프다.",
    n=1,
    size="1024x1024",
)
print(img_gt)
