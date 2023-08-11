from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Restraunt

# Core functions
from core import views as CORE_VIEWS

# Restraunts home.
def restraunts( request ):
    restraunts  = Restraunt.objects.all()
    context     = {'segment': 'index', "restraunts": restraunts}
    context     = CORE_VIEWS.context_maker(request, context)

    #########################
    # Default renderer, replaced by core standard to take advantage of in10ln
    # return render( request, "restraunts/index.html", {"restraunts": restraunts})
    #########################
    html_template = loader.get_template('restraunts/index.html')
    return HttpResponse(html_template.render(context, request))
    

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
    
    context     = {}

    if request.method == "GET":
        html_template = loader.get_template('restraunts/index.html')
    else:
        restraunt = request.POST.get("name", "")
        if len(restraunt):
            try:
                rest = Restraunt(name=restraunt)
                rest.save()
                context.update({"success": True})
            except:
                context.update({"fail": True})
        else:
            context.update({"fail": True})
    context     = CORE_VIEWS.context_maker(request, context)
    html_template = loader.get_template('restraunts/add.html')

    # Return the response once
    return HttpResponse(html_template.render(context, request))
    