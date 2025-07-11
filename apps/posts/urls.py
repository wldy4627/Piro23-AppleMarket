from django.urls import path
from apps.posts import views

urlpatterns = [
    path('', views.main),
    path('posts/create', views.create),
]