from django.conf import settings
from django.db import models
from django.utils import timezone

# python -m venv
# -m 모듈

# Post가 Model을 상속받는다.
# 상속 Model의 속성이나 메서드를 Post에서 그대로 쓸 수 있다.
# 현실 세계의 상속
# Model이 부모 클래스

class Post(models.Model):
    # 속성
    # 외래키 다른 모델을 가리키는 속성, on_delete author가 지워졌을 경우 Post 테이블의 데이터
    # CASCADE는 author가 지워지면 post도 지워지게 
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField 제목이 200자 CharField란 길이가 정해져있는 문자열을 담을 때
    title = models.CharField(max_length=200)
    # TextField 길이가 정해져 있지 않은 문자열
    text = models.TextField()
    # 날짜 그리고 시간
    # timezone.now 기본값이 현재시각
    created_date = models.DateTimeField(
            default=timezone.now)
    # 게시글이 퍼블리시된
    published_date = models.DateTimeField(
            blank=True, null=True)

    # 메서드
    def publish(self):
        # self 자기 자신의 오브젝트를 가리키는 약속
        self.published_date = timezone.now()
        # Post가 실제로 데이터베이스에 저장이 된다.
        self.save()

    # 메서드
    # __str__
    # str(3) -> '3'
    # post = Post()
    # post.title = '게시글'
    # print(post) -> 게시글
    def __str__(self):
        return self.title