from django.db import models

# Create your models here.
class House(models.Model):

    """House Model Definition"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="price",help_text="Price per night")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True ,help_text="Are pets allowed?")


    def __str__(self):
        return self.name