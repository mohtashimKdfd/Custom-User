from django.shortcuts import render
from rest_framework import generics , mixins

from main.serializers import UserSerializer
from .models import User
from django.http import JsonResponse
import json 
# Create your views here.

class NewUser(generics.GenericAPIView):
    def post(self,request):
        body = json.loads(request.body.decode('utf-8'))
        username = body['username']
        email = body['email']
        password = body['password']
        mobile = body['mobile']

        new = User(username=username, email=email,mobile=mobile,password=password,is_staff=True,is_admin=True,is_superuser=True,is_active=True)

        new.save()
        new.set_password(new.password)
        new.save()

        return JsonResponse('Naya user bangaya hai bhai',safe=False,status=201)
    # def get(self,request):
    #     serialized = UserSerializer(User.objects.al())