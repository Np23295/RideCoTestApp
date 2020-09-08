# Generated by Django 2.2.12 on 2020-09-07 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_auto_20200907_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedmaps',
            name='locations',
        ),
        migrations.AddField(
            model_name='maps',
            name='shared_with',
            field=models.ManyToManyField(to='maps.SharedMaps'),
        ),
        migrations.AlterField(
            model_name='sharedmaps',
            name='shared_with',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
