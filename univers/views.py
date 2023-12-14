from django.shortcuts import render

def home(request):
    return render(request, 'univers/home.html')

def about_us(request):
    return render(request, 'univers/about.html')

def abiturientlar(request):
    return render(request, 'univers/abiturientlar.html')

def contacts(request):
    return render(request, 'univers/contacts.html')

def habarlar(request):
    return render(request, 'univers/habarlar.html')

def meyilnamalar(request):
    return render(request, 'univers/meyilnamalar.html')