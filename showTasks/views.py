from django.shortcuts import redirect, render
from django.http import HttpResponse
from createTasks.models import tache, tacheAFaire, tacheTerminee



def inittache ():
    ls = tache()
    ps = tacheAFaire()
    rs = tacheTerminee()
    ls.nomDeTache = "rien"
    ps.nomDeTache = "rien"
    rs.nomDeTache = "rien"
    ls.etatTache = "rien"
    ps.save()
    rs.save()
    ls.save()
    return redirect ("/")


# Create your views here.
def index(request):
    

    if tache.objects.exists() and tacheAFaire.objects.exists() and tacheTerminee.objects.exists():
        now = tache.objects.all()
        nexte = tacheAFaire.objects.all()
        ende = tacheTerminee.objects.all()
        return render(request, 'show.html', {'maintenant':now, 'apres':nexte, 'fini':ende})
    else:
        inittache()
        


def change(request, indentification):
    yes=tache.objects.get(pk=indentification)
    if(yes.nomDeTache != "rien"):
        ls = tacheAFaire()
        print(yes.nomDeTache)
        ls.nomDeTache = yes.nomDeTache
        ls.save()
        yes.delete()
    return redirect ("/")

def changer(request, indentification):
    yes=tacheAFaire.objects.get(pk=indentification)
    if(yes.nomDeTache != "rien"):
        ls = tacheTerminee()
        print(yes.nomDeTache)
        ls.nomDeTache = yes.nomDeTache
        ls.save()
        yes.delete()
    return redirect ("/")