from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),  
    path('encrypt/', views.encrypt_view, name='encrypt_view'),  
    path('decrypt/', views.decrypt_view, name='decrypt_view'),  
]
