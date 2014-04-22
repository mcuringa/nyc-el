https://docs.djangoproject.com/en/dev/ref/models/fields/
from django.db import models

class City(models.Model):
  
  name = models.CharField(max_length = 50)
  population = models.IntegerField(default = 0)
  square_miles = models.IntegerField(default = 0)
  square_miles_track = models.IntegerField(default = 0)
  avg_annual_riders = models.IntegerField(default = 0)
  cost_tix = models.Float(default = 0) -----find decimal
  num_stations = models.IntegerField(default = 0)
  
# This is a guess v ----- I don't really know what's up ---------------------

  # storedCity = models.DateTimeField(auto_now_add= True)
  # parent = models.pForeignKey(City)

  # def storedCity(self, newCity):

  #   self.name = newCity.name
  #   self.population = newCity.population
  #   self.square_miles = newCity.square_miles
  #   self.square_miles_track = newCity.square_miles_track
  #   self. avg_annual_riders = newCity.avg_annual_riders
  #   sef.cost_tix= newCity.cost_tix
  #   self. num_stations= newCity.num_stations
#------------------------------------------------------------------------------------
  
  
class Stations(models.Model):
  key_facts = models.CharField(max_length=500)
  ownership = models.CharField(max_length= 500)
  percent_grwth = models.IntegerField(default = 0 )
  yr_built = models.CharField(default = 0)
    
# Also a guess... still don't know ------------------

  # def storedStations(self, newStation):
  #   self.key_facts = newStation.key_facts
  #   self.ownership = newStation.ownership
  #   self.percent_grwth = newStation.percent_grwth
  #   self.yr_built = newStation.yr_built
  
#------------------------------------------------------------------------------------
