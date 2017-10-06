from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')