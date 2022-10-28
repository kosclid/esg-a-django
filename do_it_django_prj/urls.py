"""do_it_django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from django.http import HttpResponse


# from django.conf.urls.static import static
# from django.conf import settings



def root(request):
    return HttpResponse('hello django')


urlpatterns = [
    path('', root),
    path('blog/', include('blog.urls')),
    path('diary/', include('diary.urls')),
    path("admin/", admin.site.urls),  # path('이 주소가 들어오면', 이 함수에서 처리할 것이다.)
]

# 정적파일 서빙 기능은 장고 개발서버에서 디폴트로 지원 => 실서비스 모드에서는 자동으로 꺼짐.
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
