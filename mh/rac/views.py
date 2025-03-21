from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ConcernForm, EditConcernForm
from base.models import Profile



@login_required(login_url='/login')
def rac(request):
    form = EditConcernForm()

    #if the post request is valid, save the workshop
    if request.method == "POST":
        form = EditConcernForm(request.POST)
        if form.is_valid():

            #redirect to the workshops page
            profile = form.save()
            return redirect ("personalPlan",pk=profile.id)


    #render the workshop form webpage
    context = {'form':form}
    return render(request, 'rac/rac.html',context)
  
    