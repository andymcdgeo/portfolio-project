from django.shortcuts import render
from .models import Publications

# Create your views here.

def allpublications(request):
    publications = Publications.objects
    return render(request, 'publications/publications.html', {'publications':publications})
