from rest_framework import serializers
from .models import Scores

class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scores
        fields = ['wrapper', 'band', 'firmness', 'oils', 'light', 'burn', 'draw', 'consistency', 'flavor', 'smoothness', 'blend', 'progression', 'finish', 'speed', 'price', 'overall', 'cigar']
        depth = 1
        