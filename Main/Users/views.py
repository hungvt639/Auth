from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework import generics
from .models import MyUsers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, CreateUserSerializer
from rest_framework import permissions
# Create your views here.


class UserList(generics.ListAPIView):
    queryset = MyUsers.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = MyUsers.objects.all()
    serializer_class = UserSerializer


class Profile(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return Response({"hello": "helll1"})


class CreateUser(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        user = MyUsers()
        username = request.POST['username']
        print(username)
        d={"data": username}
        return Response(d)