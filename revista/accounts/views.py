from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.core.mail import send_mail
import random
from django.forms import ValidationError

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import PasswordResetCode, User

# Create your views here.

# login class view
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        elif not user.is_active:
            return Response({'error': 'Your account is inactive'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response = Response({'access_token': access_token}, status=status.HTTP_200_OK)
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True, samesite='Strict')
            return response
       
class RefreshTokensView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if refresh_token is None:
            return Response({'error': 'No refresh token provided'}, status=400)
        try:
            RefreshToken(refresh_token)
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=400)
        try:
            token = RefreshToken(refresh_token)
            new_access_token = str(token.access_token)
            new_refresh_token = str(token)
            response = Response({'access_token': new_access_token, 'refresh_token': new_refresh_token})
            response.set_cookie(key='refresh_token', value=new_refresh_token, httponly=True, samesite='Strict')
            return response
        except Exception as e:
            return Response({'error': 'Failed to refresh tokens'}, status=400)

# Reset password views
# 1.take the username and send an email
class ForgetPasswordView(APIView):
    def post(self, request):
        username = request.data.get('username')
        
        if not username:
            return Response({"error": "username required"}, status=status.HTTP_400_BAD_REQUEST)
       
        try:  
            user = User.objects.get(username=username)            
            id = user.id
            email = user.email
        except user.DoesNotExist:
            return Response({"error": "user with that username doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
          
        # Delete all old password reset codes for the user
        PasswordResetCode.objects.filter(user=user).delete()
             
        # create a new code   
        def generate_random_code():
            code = ""
            for i in range(6):
                code += str(random.randint(0, 9))
            return code
            
        code = generate_random_code()
        reset_code = PasswordResetCode.objects.create(user=user, code=code)
        
        # send an email
        subject = 'Verify Code'
        message = f'This is your verification code for revista: {code}\nif you haven\'t request for it, ignore it'
        from_email = 'settings.EMAIL_HOST_USER'
        recipient_list = [email]
           
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        return Response({'id': id, 'email': email}, status=status.HTTP_200_OK)
  
# 2.check if the code is correct      
class CheckCodeView(APIView):
    def post(self, request):
        sent_code = request.data.get('code')
        if not sent_code:
            return Response({"error": "code required"}, status=status.HTTP_400_BAD_REQUEST)
         
        try:
            code = PasswordResetCode.objects.get(code=sent_code)
        except PasswordResetCode.DoesNotExist:
            return Response({"error": "wronge code"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message" : "successful"}, status=status.HTTP_200_OK)
        
# 3.reset the password in the database
class ResetPasswordView(APIView):
    def post(self, request):
        id = request.data.get('id')
        new_password = request.data.get('password')
        
        # checking for the input
        if not id:
            return Response({"error": "id required"}, status=status.HTTP_400_BAD_REQUEST)
        if not new_password:
            return Response({"error": "password required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(id=id)
        if user is None:
            return Response({"error": "No user exist with that id"}, status=status.HTTP_400_BAD_REQUEST)
        
        # password validation
        try:
            validate_password(new_password, user=user)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)
        
        # reset password
        user.set_password(new_password)
        user.save()
        
        return Response({"message" : "successful"}, status=status.HTTP_200_OK)


        