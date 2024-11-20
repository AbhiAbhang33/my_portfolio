from django.shortcuts import render

# Create your views here.
def home(request=None):
    return render(request, 'home.html')
