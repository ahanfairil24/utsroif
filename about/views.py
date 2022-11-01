from django.shortcuts import render

def index(request):
    return render(request, 'about/plengngen.html')

# Create your views here.