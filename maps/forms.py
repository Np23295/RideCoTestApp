from django.contrib.gis import forms

from maps.models import Maps


class MapsForm(forms.ModelForm):
    class Meta:
        model = Maps
        fields = ('label', 'point', 'shared_with')
        widgets = {
            'point': forms.OSMWidget(
                attrs={
                    'map_width': 1920,
                    'map_height': 1080,
                    'template_name': 'gis/openlayers-osm.html',
                    'default_lat': 43.452969,
                    'default_lon': -80.495064,
                    'default_zoom': 9
                }
            )
        }


