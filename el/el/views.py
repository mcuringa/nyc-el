from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    """The home page"""
    x= 2 **16
    context = {"math_prob": x}
        
    return render(request, 'home.html', context)

def link1(request):
    """The first linked page"""
    term = "adelphi"
    context = {}

    if term == "adelphi":
        context["city"]= "garden city"
        context["size"]= "15,000"

    else:
        context["city"] = "??"
        context["size"] = "-1"
    
    return render(request, 'home.html', context)

def link2(request):
    """The second linked page"""

    userput = "soccer"

    sport = {"soccer": ["red bulls", "nyc fc"], "basketball": ["knicks", "nets"]}

    data = {}
    data["sport"] = sport[userput]

    return render(request, 'home.html', data)
    
def tokyo(request):
    """The third linked page"""
    
    return render(request, 'tokyo.html')
    
def link4(request):
    """The tested linked page"""
    
    return render(request, 'home.html')
    
def link5(request):
	"""I'm testing the github deal I downloaded to my computer now"""
	
	return render(request, 'home.html')
