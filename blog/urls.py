from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #i want to create a function and giving the path a name
]
