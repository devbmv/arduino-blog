from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_blog, name='my_blog'),
    # Adaugă alte căi aici
]
