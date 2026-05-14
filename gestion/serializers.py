from rest_framework import serializers
from .models import Produit, Client, Vente, AuditVente

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = '__all__'

class AuditVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditVente
        fields = '__all__'
