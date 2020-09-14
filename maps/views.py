from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
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


def addmap(request):
    if request.method == 'POST':
        print("POST Called", request.POST)
        # obj = request.POST
        # obj.__dict__.pop('csrfmiddlewaretoken', None)
        point = request.POST.get('point')
        print(point)
        if not point:
            raise ValidationError("You have forgotten to select location!")
        label = request.POST.get('label')
        shared_with = request.POST.get('shared_with')
        users = User.objects.filter(id__in=shared_with)
        res = Maps(point=point, label=label)
        res.save()
        res.shared_with.set(users)
        # res = Maps.objects.create(obj)
        print(res)
    else:
        print("Other method called")
    return index(request)