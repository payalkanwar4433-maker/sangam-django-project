from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

def service(request):
    return render(request, "serves.html")

@api_view(['GET'])
def test_api(request):
    return Response({"message": "AI App API working"})

@api_view(['GET'])
def service_api(request):
    return Response({
        "title": "Our Services",
        "services": [
            "Web Development",
            "AI Tools",
            "Automation"
        ]
    })

@api_view(['GET'])
def about_api(request):
    return Response({
        "title": "About Us",
        "description": "We are Sangam University project"
    })

@api_view(['GET'])
def contact_api(request):
    return Response({
        "email": "info@sangam.com",
        "phone": "+91-9999999999"
    })

def api_page(request):
    return render(request, "app.html")
