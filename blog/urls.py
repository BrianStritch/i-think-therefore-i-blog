from . import views  # the . means from this directory (blog) import views.py
from django.urls import path


urlpatterns = [
    path('',  views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
