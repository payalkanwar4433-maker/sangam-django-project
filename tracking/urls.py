from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add_shipment),
    path('track/<str:tracking_id>/', views.track_shipment),
]
