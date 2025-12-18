from django.db import models

# Create your models here.

class Shipment(models.Model):
    tracking_id = models.CharField(max_length=50, unique=True)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=50,
        choices=[
            ('Booked', 'Booked'),
            ('In Transit', 'In Transit'),
            ('Out for Delivery', 'Out for Delivery'),
            ('Delivered', 'Delivered'),
        ]
    )
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tracking_id
