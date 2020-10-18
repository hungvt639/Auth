from rest_framework import generics
from .models import MyUsers
from rest_framework.response import Response
from .serializer import UserSerializer, CreateUserSerializer, EditUserSerializer, ChangePassworSerializer
from rest_framework import permissions, status, parsers
from .permissions import user_permission


class Profile(generics.ListCreateAPIView):
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser, )

    def get(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(request.user)
            res = {'data': serializer.data}
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            respone = {"message": "Error"}
            return Response(respone, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            user = request.user
            serializer = EditUserSerializer(user, request.data)
            if serializer.is_valid():
                serializer.save()
                user = serializer.data.copy()
                return Response(user, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            respone = {"message": "Error"}
            return Response(respone, status=status.HTTP_404_NOT_FOUND)


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
                return Response({"user": user}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise e
            respone = {"message": "Error"}
            return Response(respone, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            old_password = request.data['old_password']
            if user.check_password(old_password):
                user.set_password(request.data['password'])
                user.save()
                respone = {"message": "Update password successfully."}
                return Response(respone, status=status.HTTP_200_OK)
            else:
                respone = {"message": "Your old password was entered incorrectly. Please enter it again."}
                return Response(respone, status=status.HTTP_400_BAD_REQUEST)
        except:
            respone = {"message": "Error"}
            return Response(respone, status=status.HTTP_404_NOT_FOUND)


class Logout(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
