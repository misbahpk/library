from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home_templates/index.html')

def main(request):
    return render(request,'home_templates/main.html')