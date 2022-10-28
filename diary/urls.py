from django.urls import path
from diary import views

urlpatterns = [
        path('', views.index),
        path('<int:pk>/', views.dia_detail),
        path('new/', views.dia_new),
        path('<int:pk>/edit/', views.dia_edit),
        path('<int:pk>/delete/', views.dia_delete),

]

