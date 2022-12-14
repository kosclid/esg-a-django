from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
    # <int:pk> blog/ 뒤에 숫자가 들어온다면 이걸 pk로 뒤함수에 넘길기고 뒤 함수를 실행할 것이다.
    # int : nd이면 n을 뒤 함수에 넘긴다.
    path('new/', views.post_new),
    path('restaurants/', views.rest_list),
    path('restaurants/<int:pk>/', views.rest_post),
    path('restaurants/rest_new/', views.rest_new),

]

