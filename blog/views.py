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

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)  # pk=10인 포스트 가져옴->위에서 pk를 받으므로 pk=pk로 쓸 수 있음 앞의pk와 뒤의 pk는 다른의미
    return render(
    request, 
    "blog/single_post_page.html",
    {'post' : post,
    })
