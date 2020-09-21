from .models import MyUsers
from rest_framework import serializers
from App.models.Snippets import Snippet



class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = MyUsers
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUsers
        fields = ['id', 'username', 'password','email', 'first_name', 'last_name', 'phone', 'sex', 'address', 'birthday']
        write_only_fields = ('password', )
        read_only_fields = ('id', )

    def create(self, validated_data):
        user = MyUsers.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            sex=validated_data['sex'],
            address=validated_data['address'],
            birthday=validated_data['birthday']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        pass
