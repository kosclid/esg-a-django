from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목 저장
    content = models.TextField()  # 내용 저장 

    created_at = models.DateTimeField()  # 생성된 시각 저장

    def __str__(self):
        return self.title



