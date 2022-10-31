from importlib.resources import path
from django.urls import path
from .import views
#listview k liya for class view
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, UserPostListView )


urlpatterns = [
    path('', PostListView.as_view(), name='Home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    # post k andr pk mean primary key and int mean intger 
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about'),
] 