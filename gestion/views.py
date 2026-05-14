from django.shortcuts import render
from rest_framework import viewsets
from .models import Produit, Client, Vente, AuditVente
from .serializers import ProduitSerializer, ClientSerializer, VenteSerializer, AuditVenteSerializer

# Create your views here
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer

class AuditVenteViewSet(viewsets.ModelViewSet):
    queryset = AuditVente.objects.all()
    serializer_class = AuditVenteSerializer
