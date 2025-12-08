from .models import Mody
from rest_framework import serializers


class ModySerializer(serializers.ModelSerializer   ):
    class Meta:
        model = Mody
        fields = '__all__'

