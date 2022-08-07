from rest_framework import serializers

from .models import (Truck, Customer, Cargo, 
                     Category, Driver, Location, 
                     Invoice, WayBill, Order )

class TruckSerialaizer(serializers.ModelSerializer):
    
    class Meta:
        model = Truck
        fields = '__all__'
        
class InvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invoice
        fields = '__all__'
        
class OrderSerialaizer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
        
class DriverSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Driver
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Location
        fields = '__all__'
        
class CargoSerializer(serializers.ModelSerializer):
    
    category = serializers.StringRelatedField()
    
    class Meta:
        model=Cargo
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Customer
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields = '__all__'
        
class WayBillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=WayBill
        fields = '__all__'