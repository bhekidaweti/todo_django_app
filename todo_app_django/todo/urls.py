from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task', views.create_task, name='create_task'),
    path('delete/<int:todo_id>/', views.delete_task, name='delete_task'),
] 