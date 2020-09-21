from rest_framework import generics
from .models import MyUsers
from rest_framework.response import Response
from .serializer import UserSerializer, CreateUserSerializer
from rest_framework import permissions
from .permissions import user_permission



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
        try:

            serializer = CreateUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = serializer.data.copy()
                user.pop('password')
                user_permission(user['id'])
                return Response({'user': user})
            else:
                return Response(serializer.errors)
        except Exception as e:
            raise e


class TestPerm(generics.ListCreateAPIView):

    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        user_permission(3)
        return Response({'OK': "OKKK"})
