from rest_framework import serializers
from .models import Services, Payment_User, User

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class Payment_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    