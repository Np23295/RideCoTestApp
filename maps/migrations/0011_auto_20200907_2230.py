# Generated by Django 2.2.12 on 2020-09-07 22:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0010_auto_20200907_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_with', to=settings.AUTH_USER_MODEL),
        ),
    ]
