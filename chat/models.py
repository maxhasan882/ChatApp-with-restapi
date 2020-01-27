from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Chat(models.Model):
    name = models.CharField(max_length=300, null=False, blank=True)
    participants = models.ManyToManyField(User, related_name='partner')

    def __str__(self):
        if self.name == "":
            return str(self.pk)
        else:
            return self.name


class Message(models.Model):
    massage_body = models.CharField(max_length=300, blank=False, null=False)
    time = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    chat = models.ForeignKey(Chat, null=False, on_delete=models.CASCADE)
    seen = models.ManyToManyField(User, related_name='seen', blank=True)

    def __str__(self):
        return self.massage_body[:10]
