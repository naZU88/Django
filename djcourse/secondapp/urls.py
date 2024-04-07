from django.urls import path
from .views import client_orders_week, client_orders_month, client_orders_year, upload_product
urlpatterns = [
    path('week/<int:client_id>', client_orders_week, name='week'),
    path('month/<int:client_id>', client_orders_month, name='month'),
    path('year/<int:client_id>', client_orders_year, name='year'),
    path('product/', upload_product, name='product'),
]