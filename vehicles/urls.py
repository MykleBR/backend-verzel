from django.urls import path
from .views import VeiculoListCreateView, VeiculoRetrieveUpdateDestroyView

urlpatterns = [
    path('veiculos/', VeiculoListCreateView.as_view(), name='veiculo-list-create'),
    path('veiculos/<int:id>/', VeiculoRetrieveUpdateDestroyView.as_view(), name='veiculo-detail'),
]