from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ScoresSerializer
from .models import Scores

# Create your views here.

@api_view(['GET'])
def scores_list(request):

    if request.method == 'GET':
        queryset = Scores.objects.all()
        serializer = ScoresSerializer(queryset, many=True)
        return Response(serializer.data)