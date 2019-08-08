from rest_framework import serializers
from .models import CustomUser


class GetUsers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name')
