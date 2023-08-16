from rest_framework import routers,serializers,viewsets
from .models import Score

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ['x', 'y', 'user_id']