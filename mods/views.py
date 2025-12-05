from django.shortcuts import render
from .models import Mody
from rest_framework import viewsets
from mods.serializer import ModySerializer


class ModyViewSet(viewsets.ModelViewSet):
    queryset = Mody.objects.all()
    serializer_class = ModySerializer













# Create your views here.
