from rest_framework import generics
from .models import Pereval
from .serializers import PerevalSerializer

class PerevalListCreateView(generics.ListCreateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer