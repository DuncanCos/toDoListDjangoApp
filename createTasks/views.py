from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import NameForm
from .models import tache,tacheAFaire,tacheTerminee

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            ls=tache()
            ls.nomDeTache = form.cleaned_data["nomDeTache"]
            #ls.etatTache = "a faire"
            ls.save()
            return redirect ("/")
    else:
        form = NameForm()

    return render (request, "index.html",{ "form":form})