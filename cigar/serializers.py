from rest_framework import serializers
from .models import Cigar

class CigarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cigar
        fields = ['company', 'brand', 'gauge', 'length']