from django.db import models

# Data model representing tour dates
class Tour_Dates(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=50)
    coords_x = models.DecimalField(max_digits=8, decimal_places=4)
    coords_y = models.DecimalField(max_digits=8, decimal_places=4)
    special_guest = models.CharField(max_length=50, null=True)