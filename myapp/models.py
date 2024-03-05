from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)



class EncryptionKey(models.Model):
    encrypted_text = models.CharField(max_length=1024)
    encryption_key = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.encrypted_text
