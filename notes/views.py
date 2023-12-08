from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotesSerializer
from .models import Notes

# Create your views here.

@api_view(['GET'])
def notes_list(request):

    if request.method == 'GET':
        queryset = Notes.objects.all()
        serializer = NotesSerializer(queryset, many=True)
        return Response(serializer.data)