from django.contrib import admin
from .models import UserProfile, EncryptionKey
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(EncryptionKey)
