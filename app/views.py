# filepath: [views.py](http://_vscodecontentref_/1)
from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contacts(request):
    return render(request, 'app/contacts.html')

def products(request):
    return render(request, 'app/products.html')

def students(request):
    return render(request, 'app/students.html')

def profile(request):
    context = {
        'name': 'Іван',
        'age': 18,
        'city': 'Київ'
    }
    return render(request, 'app/profile.html', context)

def sales(request):
    return render(request, 'app/sales.html')