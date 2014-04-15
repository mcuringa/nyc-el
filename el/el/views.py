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
    
def link3(request):
    """The third linked page"""

    # userInput = buttonSelection  <---This is what I need to use eventually
    # This is for the test   V

    # userInput= ""
    
    # data = {"londonbutton" : ["london- cityname", "population#", "location", "ranking in largest transit systems"], "moscowbutton": ["rio-cityname","pop#2", "loc2", "rank2"]}

    # "radio1" = data[londonbutton]
    # "radio2" = data[moscowbutton]

    # if userInput == "radio1"

    # if buttonSelection == londonbutton
    #     data["londonbutton"] = ""

    
    # return render(request, 'home.html', data)


    # userInput= ""
# <a href="http://jquery.com/">jQuery</a>
#  <script src="jquery.js"></script>
# <script>
#     if(document.getElementByID('city_london').checked){
#         userInput = "radio1"

#     }else if(document.getElementById('city_moscow').checked)
#         userInput = "radio2"
# </script>

    #     data[londonbutton]



# <a href="http://jquery.com/">jQuery</a>
#  <script src="jquery.js"></script>

#     <script>
#         function check_value(val){    
#         var cities = ["london", "moscow"];
#         var city = cities[val];
#         var el = document.getElementById("postcard");
#         if (city){
#         el.src = 
#         }




# Can the dictionary information be organized into a class system?
    # class PostCardData:

    #     def __init__(self):
    #         self.city = "cityName"
    #         self.pop = "population"
    #         self.location = "countryName"
    #         self.transit = "transitTypes/Rank/ ?"

    # london = PostCardData()
    #     london.city = "london"
    #     london.pop = "8.174 million"
    #     london.location = "England"
    #     london.transit ="track=402 km"

    # moscow = PostCardData()
    #     moscow.city = "moscow"
    #     moscow.pop = "11.5 million"
    #     moscow.location: "Russia"
    #     moscow.tranit= "route=325.4 km"


def link4(request):
    """The tested linked page"""
    
    return render(request, 'home.html')
    
def link5(request):
	"""I'm testing the github deal I downloaded to my computer now"""
	
	return render(request, 'home.html')