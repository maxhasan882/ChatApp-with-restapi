from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='index'),
    path('test/', views.test, name='test'),
    path('chat-list/', views.ChatView.as_view(), name='chat-list'),
    path('room/<str:room_name>/', views.room, name='room'),
]
