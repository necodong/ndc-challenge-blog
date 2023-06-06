# ndc-challenge-blog

## .env 파일 세팅 방법
* env.sample 파일을 .env 파일로 복사합니다.
* .env 파일을 아래와 같이 편집합니다.
  * DJANGO_SECRET_KEY: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
  * OPENAI_API_KEY: https://platform.openai.com/account/api-keys 에서 키를 받아옵니다.
  * REQUESTS_CA_BUNDLE: 사설 인증서를 사용할 경우 인증서 경로를 넣어둡니
