from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField(validators=[MinValueValidator(0)])

    def get_item(self):
        return f'{self.Title}:{str(self.Price)}'

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    BookingDate = models.DateTimeField()

