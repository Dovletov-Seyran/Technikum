from django.shortcuts import render
from .models import Category, News

def home(request):
    news = News.objects.all()[0:2]
    context = {'news': news}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def abiturientlar(request):
    return render(request, 'abiturientlar.html')

def contacts(request):
    return render(request, 'contacts.html')

def habarlar(request):
    news = News.objects.all()[0:2]
    context = {'news': news}
    return render(request, 'habarlar.html', context)

def meyilnamalar(request):
    return render(request, 'meyilnamalar.html')

def more_news(request):
    return render(request, 'more_news.html')
