from django.urls import path
from apps.posts import views

urlpatterns = [
    path('', views.main),
    path('posts/create', views.create),
    path('posts/detail/<int:pk>', views.detail),
    path('posts/update/<int:pk>', views.update),
]