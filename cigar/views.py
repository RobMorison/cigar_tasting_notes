from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CigarSerializer
from .models import Cigar

# Create your views here.

@api_view(['GET'])
def cigar_list(request):

    if request.method == 'GET':
        queryset = Cigar.objects.all()
        serializer = CigarSerializer(queryset, many=True)
        return Response(serializer.data)