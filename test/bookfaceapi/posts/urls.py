from django.urls import path
from django.contrib import admin

from .views  import *

urlpatterns = [
    path('hello/',hello_world,name="hello_world"),
    path('posts/',post_list,name="post_list"),

]