# views.py
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import PersonForm

def person_create_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/') 
    else:
        form = PersonForm()
    
    return render(request, 'icard/icard.html', {'form': form})
