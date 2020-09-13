from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from maps.forms import MapsForm
from maps.models import Maps


def index(request):
    maps_list = Maps.objects.all()
    template = loader.get_template('index.html')
    context = {
        'maps_list': maps_list,
    }
    # return HttpResponse(template.render(context, request))
    form = MapsForm()
    return render(request, 'index.html', {'form': form})