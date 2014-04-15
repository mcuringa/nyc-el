from django.db import models

class City(models.Model):
  
  name = models.CharField(max_length = 50)
  population = models.IntegerField(default = 0)
  square_miles = models.IntegerField(default = 0)
  square_miles_track = models.IntegerField(default = 0)
  avg_annual_riders = models.IntegerField(default = 0)
  cost_tix = models.IntegerField (default = 0) -----find decimal
  num_stations = models.IntegerField(default = 0)
  
  
  
  
class Stations(models.Model):
  key_facts = models.CharField(max_length=500)
  ownership = models.CharField(max_length= 500)
  percent_grwth = models.IntegerField(default = 0 )
  yr_built = models.CharField(default = 0)
    