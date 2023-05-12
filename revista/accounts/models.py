from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
 
# Create your models here.

class User(AbstractUser):
    birth_date = models.DateField(null=True)
    phone_number = PhoneNumberField(null=True, blank=False, unique=True)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(null=True, max_length=1, choices=gender_choices)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    cover_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField()
    followers_count = models.IntegerField()
    following_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
      return f'{self.user.username} Profile'
