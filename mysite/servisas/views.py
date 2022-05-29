from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AutomobilioModelis, Automobilis, Paslauga, Užsakymas, UžsakymoEilutė
from django.views import generic

def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    automobilių_kiekis = Automobilis.objects.count()
    paslaugų_kiekis = Paslauga.objects.all().count()

    # Laisvos knygos (tos, kurios turi statusą 'g')
    užsakymų_kiekis = Užsakymas.objects.filter(status__exact='p').count()


    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'užsakymų_kiekis': užsakymų_kiekis,
        'paslaugų_kiekis': paslaugų_kiekis,
        'automobilių_kiekis': automobilių_kiekis,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)


def automobiliai(request):
    automobiliai = Automobilis.objects.all()
    context = {
        'automobiliai': automobiliai
    }
    print(automobiliai)
    return render(request, 'automobiliai.html', context=context)


def automobilis(request, automobilis_id):
    automobilis = get_object_or_404(Automobilis, pk=automobilis_id)
    return render(request, 'automobilis.html', {'automobilis': automobilis})


class UžsakymaiListView(generic.ListView):
    model = Užsakymas
    template_name = 'užsakymai.html'


class UžsakymasDetailView(generic.DetailView):
    model = Užsakymas
    template_name = 'užsakymas.html'
