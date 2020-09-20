from .models import MyUsers
from rest_framework import serializers
from App.models.Snippets import Snippet



class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = MyUsers
        fields = ['username', 'id', 'email', 'first_name', 'last_name']