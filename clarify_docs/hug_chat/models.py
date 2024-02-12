from django.db import models
from llm_chat.models import UserData


class HugChatMessage(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='power_messages',
        null=True
    )
    message = models.CharField(max_length=512)
    answer = models.CharField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)