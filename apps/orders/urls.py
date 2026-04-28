from django.urls import path
from .views import create_order, get_orders

urlpatterns = [
    path('', get_orders),          # ✅ GET /api/orders/
    path('create/', create_order), # ✅ POST /api/orders/create/
]