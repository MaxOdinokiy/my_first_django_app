from django.urls import path
from task_manager.say_hello import views

urlpatterns = [
    path('', views.index)
]