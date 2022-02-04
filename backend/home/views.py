from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import HomePage
from .serializers import HomeSerializer

@api_view(['GET'])
def getData(request):
    items = HomePage.objects.all()
    serializer = HomeSerializer(items, many=True)
    return Response(serializer.data)
