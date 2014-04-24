from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from el.models import *


def home(request):
    """The home page"""


    return render(request, 'home.html')
  
def cityForm(request):
    """The Form Page"""

    trains = Train.objects.all()[0]
    context = {"trains": trains}
    ticket_types = {1: "$0-2", 2:"$2-4", 3:">$4"}
    context["ticket_types"]= ticket_types
        
    return render(request, 'cityFormFill.html', context)

def save_train(request):

    form= TrainForm(request.POST)

    trains= form.save()

    return HttpResponseRedirect("/")
    






#####################EXAMPLES VVVVVV ########################

# def link1(request):÷

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
