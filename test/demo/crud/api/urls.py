from django.urls import path
from api import views

urlpatterns = [
   
    path("",views.ListItemAPIView.as_view(),name="todo_list"),
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('<int:pk>/delete/', views.delete_items, name='delete-items'),
]