from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_blog, name='my_blog'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_project_post, name='create_project_post'),
    path('post/<int:post_id>/edit/',
         views.edit_project_post, name='edit_project_post'),
    path('post/<int:post_id>/delete/',
         views.delete_project_post, name='delete_project_post'),
]
