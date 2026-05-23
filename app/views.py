from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about.html')

def stats(request):
    return render(request, 'app/stats.html')

def contacts(request):
    return render(request, 'app/contacts.html')

def catalog(request):
    return render(request, 'app/catalog.html')

def news(request):
    return render(request, 'app/news.html')

def schedule(request):
    return render(request, 'app/schedule.html')

def reviews(request):
    return render(request, 'app/reviews.html')

def ebooks(request):
    return render(request, 'app/ebooks.html')

def team(request):
    return render(request, 'app/team.html')

def faq(request):
    return render(request, 'app/faq.html')

def partners(request):
    return render(request, 'app/partners.html')

def kids(request):
    return render(request, 'app/kids.html')

def cooperation(request):
    return render(request, 'app/cooperation.html')