# Generated by Django 4.2.1 on 2023-05-15 11:49

import datetime
import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_passwordresetcode_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 12, 19, 31, 773708, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'uniqe': 'This email is already linked to an account.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(error_messages={'min_length': 'The password must have at least 8 characters.'}, max_length=128, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'min_length': 'The username must have at least 4 characters.', 'uniqe': 'This username already exists.'}, help_text='Required. in range of (4-150) characters. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='username'),
        ),
    ]
