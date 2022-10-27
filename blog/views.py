from django.shortcuts import render, redirect
from blog import forms
from blog import rest_forms

from blog.models import Post, Restaurant

from django.views.generic import CreateView
from blog.forms import PostForm
from blog.rest_forms import RestForm

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


# post_new = CreateView.as_view(
#     form_class=PostForm,
#     model=Post,
#     success_url="/blog/",
# )




def post_new(request):
    # print('request.method=', request.method)
    # print('request.POST =', request.POST)
    if request.method =="GET":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():  # 유효성 검사 함수 단하나라도 통과 못하면 거짓을 반환
            #form.cleaned_data  # 유효성 검사에 통과한 값들이 저장된 dict
            post = form.save()  # ModelForm에서 지원
            # return redirect('/blog/')
            # return redirect('/blog/{post.pk}')
            # return redirect(post.get_absolute_url())
            return redirect(post)

    return render(request, 'blog/post_form.html', {
        'form' : form,
    })
# 장고는 보낼때는 Post 받을 때는 Get 방식으로 받는다.






def rest_list(request):
    rest_qs = Restaurant.objects.all().order_by('-pk')
    return render(
        request, 
        "blog/rest_list.html",
        {'rest_list' : rest_qs,
        }
        )

def rest_post(request, pk):
    rest = Restaurant.objects.get(pk=pk)  # pk=10인 포스트 가져옴->위에서 pk를 받으므로 pk=pk로 쓸 수 있음 앞의pk와 뒤의 pk는 다른의미
    return render(
    request, 
    "blog/rest_post.html",
    {'rest' : rest,
    })


def rest_new(request):
    if request.method =="GET":
        form = RestForm()
    else:
        form = RestForm(request.POST)
        if form.is_valid():  # 유효성 검사 함수 단하나라도 통과 못하면 거짓을 반환
            post = form.save()  # ModelForm에서 지원
            return redirect(post)

    return render(request, 'blog/rest_new.html', {
        'form' : form,
    })
