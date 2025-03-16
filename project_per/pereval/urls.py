from django.urls import path
from .views import  PerevalListCreateView, PerevalDetailView

urlpatterns = [
    path('submitData/', PerevalListCreateView.as_view(), name='pereval-list-create'),
    path('submitData/<int:pk>/', PerevalDetailView.as_view(), name='pereval-detail'),
]