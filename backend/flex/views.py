from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import About
from .serializers import AboutSerializer

# Create your views here.
@api_view(['GET'])
def getData(request):
    items = About.objects.all()
    serializer = AboutSerializer(items, many=True)
    return Response(serializer.data)
