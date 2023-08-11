from django.shortcuts import render, HttpResponse, redirect
from .models import Restraunt

# Create your views here.

def restraunts( request ):
    restraunts = Restraunt.objects.all()
    return render( request, "restraunts/index.html", {"restraunts": restraunts})

def delete( request, restraunt ):
    _restraunt = Restraunt.objects.get(id = restraunt)
    try:
        _restraunt.delete()
    except:
        pass
    return redirect("/restraunts")

def add( request ):
    if request.method == "GET":
        return render(request, "restraunts/add.html")
    restraunt = request.POST.get("name", "")
    if len(restraunt):
        rest = Restraunt(name=restraunt)
        rest.save()
        return render(request, "restraunts/add.html", {"success": True})
    return render(request, "restraunts/add.html")
    