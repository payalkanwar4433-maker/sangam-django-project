from rest_framework import serializers
from .models import YourModel   # apna model name yahan

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'
