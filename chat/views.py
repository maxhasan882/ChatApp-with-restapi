from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from .serializers import ChatSerializer
from rest_framework.response import Response
import json
from .models import Chat, Message

User = get_user_model()


@login_required
def home(request):
    user = request.user
    chat_list = Chat.objects.filter(participants=user)
    #print(chat_list)
    return render(request, 'index.html', {"chat_list" : chat_list})


@login_required
def room(request, room_name):
    user = request.user
    chat_list = Chat.objects.filter(participants=user)
    chat = get_object_or_404(Chat, pk=room_name)
    participants = chat.participants.all()
    data = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'participants': participants,
        'userId': mark_safe(json.dumps(request.user.pk)),
        "chat_list": chat_list
    }
    return render(request, 'room1.html', data)


def get_last_10_messages(chatId):
    message = Message.objects.filter(chat=chatId).order_by('-time')[:10]
    return reversed(message)


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)


def test(request):
    return render(request, "room1.html")


class ChatView(APIView):
    @staticmethod
    def get(request):
        user = request.user
        chat_list = Chat.objects.filter(participants=user)
        if chat_list:
            serializers = ChatSerializer(chat_list, many=True)
            return Response(serializers.data)


class ParticipantView(APIView):
    @staticmethod
    def get(request):
        data = request.data
        new_user = User.objects.create()
