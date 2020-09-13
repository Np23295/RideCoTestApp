from django.contrib.gis import forms
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from sharedmaps.models import SharedMaps


# MAPS model holding point , label, created by and whom it is shared with


class Maps(models.Model):
    label = models.CharField(default="My Location", null=False, max_length=25)
    point = models.PointField()
    created_by = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.CASCADE, )
    shared_with = models.ManyToManyField(User, related_name="shared_with", editable=True)

    def get_shared_with(self):
        # For Quick View, whom it is shared with
        return "\n".join([p.username for p in self.shared_with.all()])
