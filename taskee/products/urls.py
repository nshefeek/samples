from django.urls import path, include
from .views import product_view
urlpatterns = [
    path('', product_view, name='products'),
]
 
