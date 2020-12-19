from rest_framework.viewsets import ModelViewSet

from . import models, serializers

class PersoneViewSet(ModelViewSet):
    queryset = models.Persone.objects.all()
    serializer_class = serializers.PersoneSerializer