from django.shortcuts import render
from .models import Mody
from rest_framework import viewsets
from mods.serializer import ModySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import json

class ModyViewSet(viewsets.ModelViewSet):
    queryset = Mody.objects.all()
    serializer_class = ModySerializer
    posts = Mody.objects.all()
    serializer1 = ModySerializer(posts, many=True)
    data =serializer1.data
    with open("wynik.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

















# Create your views here.
