from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, null=True)  # Make the field nullable
    first_name = models.CharField(max_length=30, null=True)  # Make the field nullable

    def __str__(self):
        return self.user.username
    

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        'UserProfile',
        on_delete=models.CASCADE,
        related_name='chats', 
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

class File(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=255, null=True)
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        related_name='file',
        null=True
    )

    class Meta:
        ordering = ('filename',)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        related_name='questions',  
        null=True
    )
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        related_name='answers', 
        null=True
    )
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(
        'Chat',
        on_delete=models.CASCADE,
        related_name='request_chat',
        null=True
    )
    question = models.OneToOneField(
        'Question',
        on_delete=models.CASCADE,
        related_name='request',
        null=True
    )
    answer = models.OneToOneField(
        'Answer',
        on_delete=models.CASCADE,
        related_name='request',
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)