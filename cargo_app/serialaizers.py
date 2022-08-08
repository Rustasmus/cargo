from rest_framework import serializers

from .models import (Truck, Customer, Cargo, 
                     Category, Driver, Location, 
                     Invoice, WayBill, Order )

class TruckSerialaizer(serializers.ModelSerializer):
    
    curgo_category = serializers.StringRelatedField(
        read_only=True
    )
    
    class Meta:
        model = Truck
        fields = '__all__'
        
class DriverSerializer(serializers.ModelSerializer):
    
    curgo_category = serializers.StringRelatedField(
        read_only=True
    )
    
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
        
class InvoiceSerializer(serializers.ModelSerializer):
    
    cargo = CargoSerializer(
        many=True
    )
    point_a = serializers.StringRelatedField(
        read_only=True
    )
    point_b = serializers.StringRelatedField(
        read_only=True
    )
    customer = serializers.StringRelatedField(
        read_only=True
    )
    
    class Meta:
        model = Invoice
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
    
    point_a = serializers.StringRelatedField(
        read_only=True
    )
    point_b = serializers.StringRelatedField(
        read_only=True
    )
    drivers = DriverSerializer(read_only=True)
    customer = serializers.StringRelatedField(
        read_only=True
    )
    
    class Meta:
        model=WayBill
        fields = '__all__'
        
class OrderSerialaizer(serializers.ModelSerializer):
    
    way_bill = WayBillSerializer(read_only=True)
    invoice = InvoiceSerializer(many=True)
    
    class Meta:
        model = Order
        fields = '__all__'