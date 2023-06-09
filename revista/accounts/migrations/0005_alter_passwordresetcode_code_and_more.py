# Generated by Django 4.2.1 on 2023-05-14 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_passwordresetcode_delete_passwordresettoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetcode',
            name='code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='passwordresetcode',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 14, 11, 8, 41, 276140, tzinfo=datetime.timezone.utc)),
        ),
    ]
