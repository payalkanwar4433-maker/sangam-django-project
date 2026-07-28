from django.urls import path
from . import views

urlpatterns = [
    path('service/', views.service, name='service'),
    path('api/test/', views.test_api),
    path('api/services/', views.service_api),
    path('api/about/', views.about_api),
    path('api/contact/', views.contact_api),
    path('app/', views.api_page, name='app_page'),
]
