#เลขาของห้องMyapp

from django.urls import path
from .views import homepage

urlpatterns = [
    path('',homepage ), #localhost:8000 
]
