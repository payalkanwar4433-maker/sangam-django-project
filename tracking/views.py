from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Shipment
from .serializers import ShipmentSerializer



@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to Logistics Tracking API"})


@api_view(['POST'])
def add_shipment(request):
    serializer = ShipmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Shipment added successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def track_shipment(request, tracking_id):
    shipment = get_object_or_404(Shipment, tracking_id=tracking_id)
    serializer = ShipmentSerializer(shipment)
    return Response(serializer.data)
# aiapp/views.py
from django.shortcuts import render

def tracking(request):
    return render(request, 'tracking.html')
