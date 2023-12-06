from rest_framework import serializers
from .models import Scores

class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = ['id', 'wrapper', 'band', 'firmness', 'oils', 'light', 'burn', 'draw', 'consistency', 'flavor', 'smoothness', 'blend', 'progression', 'finish', 'speed', 'price', 'overall', 'cigar', 'cigar_id']
        depth = 1

    cigar_id = serializers.IntegerField(write_only=True)
        