from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (CargoApiView, CustomerApiView, DriverApiView,
                    TruckApiView, OrderApiView, InvoiceApiView,
                    WayBillApiView, CategoryApiView, LocationApiView)


router = SimpleRouter()

router.register('cargo', CargoApiView, basename='cargo')
router.register('customer', CustomerApiView, basename='customer')
router.register('truck', TruckApiView, basename='truck')
router.register('driver', DriverApiView, basename='driver')
router.register('order', OrderApiView, basename='order')
router.register('invoice', InvoiceApiView, basename='invoice')
router.register('way_bill', WayBillApiView, basename='way_bill')
router.register('category', CategoryApiView, basename='category')
router.register('location', LocationApiView, basename='location')

urlpatterns =[
    
] + router.urls