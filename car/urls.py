from django.urls import path
from .views import (
    company_list, company_create, company_update, company_delete,
    car_list, car_create, car_update, car_delete
)

urlpatterns = [
    path('', company_list, name='company_list'),
    path('companies/create/', company_create, name='company_create'),
    path('companies/update/<int:pk>/', company_update, name='company_update'),
    path('companies/delete/<int:pk>/', company_delete, name='company_delete'),
    
    path('cars/', car_list, name='car_list'),
    path('cars/create/', car_create, name='car_create'),
    path('cars/update/<int:pk>/', car_update, name='car_update'),
    path('cars/delete/<int:pk>/', car_delete, name='car_delete'),
]
