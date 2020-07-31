from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import render



class CustomAuthentication(BaseBackend):
    
    def authenticate(self,**credentials):
        try:
            return User.objects.get(email=credentials["email"])
        except:
            return None 
