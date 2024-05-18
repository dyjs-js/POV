import time
import os
from pathlib import Path
from openai import OpenAI
import environ


## 자동 해시태그 생성을 위한 코드 시작

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
api_key = env("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "내 리뷰를 기반으로 해쉬태그 5개 생성. 소설가 이름과 소설 제목은 제외. ",
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "소설가 구병모의 대표작 《아가미》가 새 옷을 갈아입었다. 《아가미》는 죽음의 문턱에서 아가미를 갖게 된 소년의 슬픈 운명을 그려낸 아름다운 잔혹동화이다. 아가미로 숨을 쉬고 눈부신 비늘을 반짝이며 깊고 푸른 호수 속을 헤엄치는 곤. 자신의 정체를 숨기고 세상과 단절된 채 살아가는 소년은 물속에서만큼은 한없는 자유를 느낀다. 곤에게 새로운 이름과 삶을 건네준 강하, 곤의 도움으로 목숨을 건진 해류. 삶이라는 저주받은 물속에서, 오늘도 그리고 내일도 간절히 숨 쉬고 싶은, 세상으로부터 버림받고 소외된 이들의 이야기가 신비롭고도 아름답게 펼쳐진다.",
                }
            ],
        },
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
print(response)
