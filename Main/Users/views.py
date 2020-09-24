from rest_framework import generics
from .models import MyUsers
from rest_framework.response import Response
from .serializer import UserSerializer, CreateUserSerializer, EditUserSerializer
from rest_framework import permissions, status
from .permissions import user_permission


class UserList(generics.ListAPIView):
    queryset = MyUsers.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = MyUsers.objects.all()
    serializer_class = UserSerializer


class Profile(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        user = request.user
        serializer = EditUserSerializer(user, request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data.copy()
            return Response(user, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                return Response({"user": user}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise e

