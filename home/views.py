from django.shortcuts import render

from .models import Visiteur
import re

# Create your views here.

def home(request):
    envoi = False
    regex = r"^[a-z0-9._-]+@[a-z0-9._-]+\.[a-z]{2,6}$"
    if request.method == 'POST':
        ml = request.POST['ml']
        if re.search(regex, ml):
            v = Visiteur(mel=ml)
            v.save()
            envoi = True
        
    return render(request, 'home/index.html', {'envoi': envoi})
