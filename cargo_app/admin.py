from django.contrib import admin
from .models import Customer, Cargo, Category, Invoice, Order, Truck, Driver, Location, WayBill
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'telephone_number',
        'passport',
        'email',
    )
    list_filter = ('create_date',)
    search_fields = (
        'name',
        'surname',
        'telephone_number',
        'passport'
    )


class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'length',
        'width',
        'hight',
        'volume',
        'weight',
        'category',
    )
    list_filter = ('create_date', 'category')
    search_fields = (
        'volume', 
        'weight', 
        'height'
    )

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = ('create_date', )
    search_fields = ('name', )

    
class TruckAdmin(admin.ModelAdmin):
    list_display = (
        'truck_number',
        'weight',
        'volume',
        'brend',
        'model',
        'vin_code',
        'get_categories'
    )
    list_filter = ('create_date', 'brend', 'volume')
    search_fields = (
        'truck_number',
        'weight',
        'model',
        'vin_code',
    )

    
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'telephone_number',
        'passport',
        'driver_license',
        'get_categories',
        'create_date',
        'update_date',
    )
    search_fields = (
        'name',
        'surname',
        'passport',
        'telephone_number',
        'driver_license',
    )
    list_filter = (
        'create_date',
        'cargo_category',
    )
       
        
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'country',
        'city',
        'address',
    )
    list_filter = (
        'country',
        'city',
        'create_date'
    )
    search_fields = (
        'country',
        'city',
        'address'
    )
       
        
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'get_cargos',
        'point_a',
        'point_b',
    )   
    list_filter = (
        'create_date',
        'point_a',
        'point_b',
    )
    search_fields = (
        'customer',
        'cargo',
        'point_a',
        'point_b',
    )
    
    
class WayBillAdmin(admin.ModelAdmin):
    list_display = (
        'drivers',
        'truck',
        'point_a',
        'point_b',
    )
    list_filter = (
        'create_date',
        'point_a',
        'point_b',
    )
    search_fields = (
        'drivers',
        'truck',
        'point_a',
        'point_b',
    )
    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'get_invoices',
        'way_bill',
    )
    list_filter = filter = (
        'create_date',
    )
    search_fields = (
        'invoice',
        'way_bill',
    )
    
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cargo, CargoAdmin) 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Truck, TruckAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(WayBill, WayBillAdmin)
admin.site.register(Order, OrderAdmin)