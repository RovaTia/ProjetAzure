from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Produit(models.Model):
    numero_produit = models.AutoField(primary_key=True)
    design = models.CharField(max_length=100)
    stock = models.IntegerField()

    def __str__(self):
        return self.design


class Vente(models.Model):
    client = models.ForeignKey(on_delete=models.CASCADE, related_name='ventes_client')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qtesortie = models.IntegerField()
    utilisateur = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ventes_utilisateur')

    def __str__(self):
        return f"{self.client.nom} - {self.produit.design}"


class AuditVente(models.Model):
    TYPE_OPERATION = (
        ('INSERT', 'Ajout'),
        ('UPDATE', 'Modification'),
        ('DELETE', 'Suppression'),
    )
    type_operation = models.CharField(max_length=10)
    date_mise_a_jour = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=100)
    design = models.CharField(max_length=100)
    qtesortie_ancien = models.IntegerField(null=True, blank=True)
    qtesortie_nouv = models.IntegerField(null=True, blank=True)
    utilisateur = models.CharField(max_length=100)