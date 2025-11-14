from django.contrib import admin
from .models import CarMake, CarModel

# Admin configuration for CarMake
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year')
    search_fields = ('name', 'description', 'country')
    list_filter = ('country',)
    ordering = ('name',)

# Admin configuration for CarModel
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id', 'price')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year', 'car_make')
    ordering = ('car_make__name', 'name', 'year')
    raw_id_fields = ('car_make',)  # Improves performance for ForeignKey selection