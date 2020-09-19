from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework import generics
from .models import MyUsers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class CreateUser(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        user = MyUsers.objects.all()
        u = {"user": user}
        return Response(u)

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        username = request.POST['username']
        print(username)
        d= {"data": username}
        return Response(d)