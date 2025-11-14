from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True, help_text="Country of origin for the car make")
    founded_year = models.PositiveIntegerField(null=True, blank=True, help_text="Year the car make was founded")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"

# CarModel model
class CarModel(models.Model):
    # Choices for car type
    CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'),
    )

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    dealer_id = models.IntegerField(help_text="ID of the dealer from Cloudant database")
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ],
        help_text="Model year (2015–2023)"
    )
    fuel_type = models.CharField(max_length=50, blank=True, help_text="e.g., Gasoline, Diesel, Electric")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Base price in USD")

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

    class Meta:
        ordering = ['car_make__name', 'name', 'year']
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"