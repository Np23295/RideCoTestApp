from django.db import models

from django.contrib.auth.models import User
# Create your models here.
# from maps.models import Maps


class SharedMaps(models.Model):
    map = models.ForeignKey('maps.Maps', editable=True, null=True, blank=True, on_delete=models.CASCADE,)
    shared_with = models.ForeignKey(User, editable=True, null=True, blank=True, on_delete=models.CASCADE,)

