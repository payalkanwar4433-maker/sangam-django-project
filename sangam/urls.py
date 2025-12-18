"""
URL configuration for sangam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconfs
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sangam import views
from .views import stock_price
from django.http import JsonResponse
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tracking.urls')),
    path('', views.home_page,name='home'),
    path('', include('aiapp.urls')), 
    path('aboutpage/', views.aboutpage,name='about'),
    path('contactdetail/', views.contactdetail,name='contact'),
    path('service/', views.service,name='service'),
    path('stock/<str:symbol>/', stock_price, name='stock_price'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



