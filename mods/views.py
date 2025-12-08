from _ast import Compare

from django.shortcuts import render
from .models import Mody
from rest_framework import viewsets
from mods.serializer import ModySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
import json

class ModyViewSet(viewsets.ModelViewSet):
    queryset = Mody.objects.all()
    serializer_class = ModySerializer
    posts = Mody.objects.all()
    serializer = ModySerializer(posts, many=True)

