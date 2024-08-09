# views.py
from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import JobShiftForm

def job_shift(request):
    if request.method == 'POST':
        form = JobShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/') # Redirect to a success page or somewhere else
    else:
        form = JobShiftForm()
    return render(request, 'shift/shift.html', {'form': form})
