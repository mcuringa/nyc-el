from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    """The home page"""
        
    return render(request, 'home.html')

def link1(request):
    """The first linked page"""
    
    return render(request, 'link1.html')

def link2(request):
    """The second linked page"""
    
    return render(request, 'link2.html')
    
def link3(request):
    """The third linked page"""
    
    return render(request, 'link3.html')
    
def link4(request):
    """The tested linked page"""
    
    return render(request, 'home.html')
