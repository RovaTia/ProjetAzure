from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProduitViewSet, ClientViewSet, VenteViewSet, AuditVenteViewSet

router = DefaultRouter()
router.register(r'produits', ProduitViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'ventes', VenteViewSet)
router.register(r'auditventes', AuditVenteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]