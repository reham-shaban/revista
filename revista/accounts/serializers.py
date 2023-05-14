from django.contrib.auth import get_user_model
from rest_framework import serializers

Usermodel = get_user_model()

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        try:
            user = Usermodel.objects.get(email=email)
        except Usermodel.DoesNotExist:
            raise serializers.ValidationError('No user found with this email address')
        attrs['user'] = user
        return attrs