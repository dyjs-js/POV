# import os
# from pathlib import Path
# from openai import OpenAI
# import environ
# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.status import HTTP_200_OK
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound, PermissionDenied

# env = environ.Env()
# BASE_DIR = Path(__file__).resolve().parent.parent
# environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
# api_key = env("OPENAI_API_KEY")

# client = OpenAI(api_key=api_key)
# # Create your views here.


# prompt = "타이타닉,영화,타이타닉은 1997년에 개봉한 미국의 로맨스/재난 영화로, 제임스 카메론 감독의 작품이다. 영화는 실제로 발생한 1912년 타이타닉호 침몰 사건을 바탕으로 하고 있으며, 여성 주인공 로즈와 남성 주인공 잭의 사랑 이야기를 중심으로 전개된다. 이 영화는 역사적 사건을 배경으로 하면서도 로맨스와 스릴러적인 요소를 풍미하며 관객들에게 강한 여운을 남기는데, 특히 타이타닉호의 침몰 장면은 화려한 시각 효과와 함께 매우 인상적이다.슬프다."


# def get_completion(prompt):
#     query = client.images.generate(
#         model="dall-e-3",
#         prompt=prompt,
#         n=1,
#         size="1024x1024",
#     )
#     response = query.data[0].url
#     print(response)


# class gptPhotoDetail(APIView):
#     permission_classes = [IsAuthenticated]
