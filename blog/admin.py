from django.contrib import admin
from .models import Post, Restaurant

admin.site.register(Post)

admin.site.register(Restaurant)

# 커밋을 위한 주석 추가