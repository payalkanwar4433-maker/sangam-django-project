from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sangam import views
from sangam.views import stock_price

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
    path('', include('aiapp.urls')),
    path('aboutpage/', views.aboutpage, name='about'),
    path('contactdetail/', views.contactdetail, name='contact'),
    path('service/', views.service, name='service'),
    path('stock/<str:symbol>/', stock_price, name='stock_price'),
    path('api/', include('tracking.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
