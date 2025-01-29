from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'FirstApp/home.html')

def about(request):
    return render(request, 'FirstApp/about.html')

def projects(request):
    return render(request, 'FirstApp/projects.html')

def skills(request):
    return render(request, 'FirstApp/skills.html')


def certifications(request):
    return render(request, 'FirstApp/certifications.html')

def contact(request):
    return render(request, 'FirstApp/contact.html')