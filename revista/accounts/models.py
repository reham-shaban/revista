from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150, blank=False, null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=True, null=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. in range of (4-150) characters. Letters, digits and @/./+/-/_ only."
        ),
        validators=[MinLengthValidator(4)],
        error_messages={
            "uniqe": _("This username already exists."),
            "min_length": _("The username must have at least 4 characters."),
        },
        blank=False,
    )
    email = models.EmailField(
        _("email address"),
        unique=True,
        blank=False,        
        error_messages={
            "uniqe": _("This email is already linked to an account."),
        },
        )
    birth_date = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)

    gender_choices = [("M", "Male"), ("F", "Female")]
    gender = models.CharField(
        _("gender"), max_length=1, null=True, blank=True, choices=gender_choices
    )

    def __str__(self):
        return self.username

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


class PasswordResetCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=30))
         
    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def __str__(self):
        return f'code: {self.code}'
    
        
