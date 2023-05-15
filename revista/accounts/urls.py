from django.urls import path
from .views import UserCreateView
from . import views

# accounts/
urlpatterns = [
   path('login/', views.LoginView.as_view()),
   path('refresh-token/', views.RefreshTokensView.as_view()),
   path('forget-password/', views.ForgetPasswordView.as_view()),
   path('check-code/', views.CheckCodeView.as_view()),
   path('reset-password/', views.ResetPasswordView.as_view()),
   path('create-account/', UserCreateView.as_view()),
]
