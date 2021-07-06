from rest_framework import serializers
from .models import Destination

class courseserielizer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        field = '__all__'
