from rest_framework import generics
from .models import Pereval
from .serializers import PerevalSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class PerevalListCreateView(generics.ListCreateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

class PerevalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    lookup_field = 'id'  # Поле для поиска объекта

class PerevalUpdateView(APIView):
    def patch(self, request, id):
        try:
            pereval = Pereval.objects.get(id=id)
        except Pereval.DoesNotExist:
            return Response(
                {"state": 0, "message": "Запись не найдена."},
                status=status.HTTP_404_NOT_FOUND
            )

        # Проверяем, что запись в статусе "new"
        if pereval.status != Pereval.NEW:
            return Response(
                {"state": 0, "message": "Запись нельзя редактировать, так как она не в статусе 'new'."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Убираем поля, которые нельзя редактировать
        if 'user' in request.data:
            del request.data['user']

        # Обновляем запись
        serializer = PerevalSerializer(pereval, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"state": 1, "message": "Запись успешно обновлена."})
        else:
            return Response(
                {"state": 0, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
class PerevalListByEmailView(generics.ListAPIView):
    serializer_class = PerevalSerializer

    def get_queryset(self):
        email = self.request.query_params.get('user__email', None)
        if email:
            return Pereval.objects.filter(user__email=email)
        return Pereval.objects.none()