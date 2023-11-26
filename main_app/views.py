from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

finches = [
    {"name": "Finch1", "color": "Pink", "size": "Big"},
    {"name": "Finch2", "color": "Orange", "size": "Small"},
    # Add more finch data dictionaries as needed
    ]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches' : finches})