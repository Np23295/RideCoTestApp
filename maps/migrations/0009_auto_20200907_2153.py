# Generated by Django 2.2.12 on 2020-09-07 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_auto_20200907_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='shared_with',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sharedmaps.SharedMaps'),
        ),
    ]
