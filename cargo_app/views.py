from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serialaizers import (CustomerSerializer, DriverSerializer, TruckSerialaizer,
                           CargoSerializer, CategorySerializer, InvoiceSerializer,
                           OrderSerialaizer, WayBillSerializer, LocationSerializer)

from .models import (Truck, Customer, Cargo, 
                     Category, Driver, Location, 
                     Invoice, WayBill, Order )


class CargoApiView(viewsets.ModelViewSet):
    
    serializer_class = CargoSerializer
    queryset = Cargo.objects.all()

class CategoryApiView(viewsets.ModelViewSet):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CustomerApiView(viewsets.ModelViewSet):
    
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    
class DriverApiView(viewsets.ModelViewSet):
    
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    
class TruckApiView(viewsets.ModelViewSet):
    
    serializer_class = TruckSerialaizer
    queryset = Truck.objects.all()
    
class OrderApiView(viewsets.ModelViewSet):
    
    serializer_class = OrderSerialaizer
    queryset = Order.objects.all()
    
class WayBillApiView(viewsets.ModelViewSet):
    
    serializer_class = WayBillSerializer
    queryset = WayBill.objects.all()
    
class InvoiceApiView(viewsets.ModelViewSet):
    
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    
class LocationApiView(viewsets.ModelViewSet):
    
    serializer_class = LocationSerializer
    queryset = Location.objects.all()