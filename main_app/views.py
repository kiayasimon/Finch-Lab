from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def finch_list(request):
    finch_data = [
        {"name": "Finch1", "color": "Pink", "size": "Big"},
        {"name": "Finch2", "color": "Orange", "size": "Small"},
        # Add more finch data dictionaries as needed
    ]

    return render(request, 'finch_list.html', {'finch_data': finch_data})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')