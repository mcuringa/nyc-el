from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from el.models import *


def home(request):
    """The home page"""

    cities = Train.objects.all()

    context={"cities": cities}
    # city=Train.objects.all()
    # context={"train":train}
    # city_type= {1: "New York", 2:"Chicago", 3:"London"}
    # context["city_type"]= city_type
    # context["pk"]=0
    
    return render(request, 'home.html', context)
  
def cityFormFill(request):
    """The Form Page"""

    trains = Train.objects.all()
    context = {"trains": trains}
    ticket_types = {1: "$0-2", 2:"$2-4", 3:">$4"}
    context["ticket_types"]= ticket_types
    context["pk"] = 0

        
    return render(request, 'cityFormFill.html', context)
    
def save_train(request):

    form= TrainForm(request.POST)

    trains= form.save()

    return HttpResponseRedirect("/")

def europe (request):
    """The Europe page"""


    return render(request, 'europe.html')

def infoDisplayer (request, pk):
    """The "postcard" with information on it."""

    train = Train.objects.get(pk=pk)

    context= {"train": train}

    return render(request, "infoDisplayer.html", context)

def search (request):
    search_param=request.POST
    user_search = search_param["search"]
    if user_search:
        train = Train.objects.get(city_name=user_search)
        if train:
            url = "/cities/" + str(train.pk)
            return HttpResponseRedirect(url)
        else:
            return render(request, "home.html", context)
    else:
        return render(request, "home.html", context)








####################EXAMPLES VVVVVV ########################



# # def link2(request):
# #     """The second linked page"""

#     # userput = "soccer"

#     # sport = {"soccer": ["red bulls", "nyc fc"], "basketball": ["knicks", "nets"]}

#     # data = {}
#     # data["sport"] = sport[userput]

#     # return render(request, 'home.html', data)
    
# def tokyo(request):
#     """The third linked page"""
#     """ Form for inputting City information"""
    
#     return render(request, 'tokyo.html')
