from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    def validate_password(self, value):
        validate_password(value)
        return value
    
    class Meta:
        model = User
        fields ='__all__'
        write_only_fields=('password')
