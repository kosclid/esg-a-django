from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)  # 제목 저장
    content = models.TextField()  # 내용 저장 

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'[{self.pk}] : {self.title}'  
        # self.id도 있다. / pk는 정수여서 걍 같이 못씀 그래서 f string 사용  
        # '저는{d}다.' 이때 d=5 (d는 변수) 기억나지??
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
        # 추후 장고의 URL Reverse 기능 사용하기




