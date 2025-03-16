from django.urls import path
from .views import  PerevalListCreateView, PerevalDetailView, PerevalUpdateView, PerevalListByEmailView

urlpatterns = [
    path('submitData/', PerevalListCreateView.as_view(), name='pereval-list-create'),
    path('submitData/<int:pk>/', PerevalDetailView.as_view(), name='pereval-detail'),
    path('submitData/<int:pk>/update/', PerevalUpdateView.as_view(), name='pereval-update'),
    path('submitData/', PerevalListByEmailView.as_view(), name='pereval-list-by-email'),
]