from django.shortcuts import render, HttpResponseRedirect
from shift.models import JobShift
from icard.models import Person
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # Fetch the Person object related to the current user
        try:
            person = Person.objects.get(user=request.user)
        except Person.DoesNotExist:
            person = None
        
        user = request.user
        first_name = user.first_name
        last_name = user.last_name
        username = user.username
        first_letter = user.username[0]
        email = user.email

        return render(request, "core/index.html", {
            'first_name': first_name,
            'last_name': last_name,
            'user_name': username,
            'email': email,
            'dp': first_letter,
            'person': person,  # Pass the filtered Person object
        })
    
def colleagues(request):
    job_shifts = JobShift.objects.all()  
    return render(request, 'core/colleagues.html', {'job_shifts': job_shifts})





