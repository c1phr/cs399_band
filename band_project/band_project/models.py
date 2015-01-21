from django.db import models

class Tour_Dates(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=50)
    special_guest = models.CharField(max_length=50, null=True)
