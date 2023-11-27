from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
# from clarify_docs import settings
# from django.contrib.auth.models import AbstractUser
# User = settings.AUTH_USER_MODEL
EXTENSIONS_IMG = ['jpeg', 'png', 'jpg', 'svg', 'gif']


class Avatar(models.Model):
    image = CloudinaryField(resource_type='auto', allowed_formats=EXTENSIONS_IMG, folder='avatars for_clarify_docs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

