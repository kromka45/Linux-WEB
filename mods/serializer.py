from .models import Mody
from rest_framework import serializers


class ModySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mody
        fields = ['mody_id','mody_date','mody_stare','mody_nowe']

