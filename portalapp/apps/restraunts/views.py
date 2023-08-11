from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Restraunt

# Create your views here.
def restraunts( request ):
    restraunts = Restraunt.objects.all()
    return render( request, "restraunts/index.html", {"restraunts": restraunts})

@login_required(login_url="/login/")
def delete( request, restraunt ):
    _restraunt = Restraunt.objects.get(id = restraunt)
    try:
        _restraunt.delete()
    except:
        pass
    return redirect("/restraunts")

@login_required(login_url="/login/")
def add( request ):
    if request.method == "GET":
        return render(request, "restraunts/add.html")
    restraunt = request.POST.get("name", "")
    if len(restraunt):
        try:
            rest = Restraunt(name=restraunt)
            rest.save()
            return render(request, "restraunts/add.html", {"success": True})
        except:
            pass
    return render(request, "restraunts/add.html", {"fail": True})
    