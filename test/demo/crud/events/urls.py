from django.urls import path
from . import views

urlpatterns = [
    path('',views.list,name="events"),
    path('detail/<str:pk>/',views.detail,name="detail"),
    path('create',views.create,name="create"),
    path('update/<str:pk>/',views.update,name="update"),
    path('delete/<str:pk>/',views.Deletes,name="delete"),
]