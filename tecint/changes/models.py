from django.db import models

# Create your models here.
class DateWeather(models.Model):
    date = models.DateField()
    was_rainy = models.BooleanField(default=False)
    def __str__(self):
        return str(self.date) + " Weather was rainy? " + str(self.was_rainy) 

class BecameBad(models.Model):
    date = models.DateField(null=True, blank=True)
    became_bad = models.BooleanField(default=True)
    def __str__(self):
        return str(self.date)