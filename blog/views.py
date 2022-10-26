from django.shortcuts import render
from blog.models import Post

def index(request):
    # 전체 포스팅을 가져올 준비(가져오기 이전임)
    post_qs = Post.objects.all().order_by('-pk')
    return render(
        request, 
        "blog/index.html",
        {'post_list' : post_qs,
        }
        )


