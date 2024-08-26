# from django.http import HttpResponse

from django.shortcuts import render
def home(request):
    # return HttpResponse('Welcome to the homepage!')
    return render(request, 'home.html')  # use the 'home.html' template

def about(request):
    # return HttpResponse('This is the about page.')
    return render(request, 'about.html')  # use the 'home.html' template