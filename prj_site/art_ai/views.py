from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('<h1>Hello, world!</h1>')

def post(request):
    form = PostForm()
    return render(request, 'art_ai/input.html', {"form":form})

def home(request):
    return render(request, 'art_ai/home.html')

def input(request):
    return render(request, 'art_ai/input.html')

def output(request):
    return render(request, 'art_ai/output.html')
