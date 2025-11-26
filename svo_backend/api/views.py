from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .models import (
    Role, Direction, Service, Utilisateur,
    LogAction, ValeurExtrait, Valeur,
    HistoriqueValeur, Validation
)

from .serializers import (
    RoleSerializer, DirectionSerializer, ServiceSerializer, UtilisateurSerializer,
    LogActionSerializer, ValeurExtraitSerializer, ValeurSerializer,
    HistoriqueValeurSerializer, ValidationSerializer
)


# =============================
#  BASE VIEWSET STANDARD
# =============================
class BaseViewSet(viewsets.ModelViewSet):
    """ViewSet de base avec authentification obligatoire."""
    permission_classes = [IsAuthenticated]


# =============================
#  ROLE
# =============================
class RoleViewSet(BaseViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# =============================
#  DIRECTION
# =============================
class DirectionViewSet(BaseViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


# =============================
#  SERVICE
# =============================
class ServiceViewSet(BaseViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


# =============================
#  UTILISATEUR
# =============================
class UtilisateurViewSet(BaseViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


# =============================
#  LOG ACTION
# =============================
class LogActionViewSet(BaseViewSet):
    queryset = LogAction.objects.all()
    serializer_class = LogActionSerializer


# =============================
#  VALEUR EXTRAIT
# =============================
class ValeurExtraitViewSet(BaseViewSet):
    queryset = ValeurExtrait.objects.all()
    serializer_class = ValeurExtraitSerializer


# =============================
#  VALEUR
# =============================
class ValeurViewSet(BaseViewSet):
    queryset = Valeur.objects.all()
    serializer_class = ValeurSerializer

    # 🔥 Route personnalisée : filtrage par HS Code
    @action(detail=False, methods=["get"])
    def search(self, request):
        hs = request.GET.get("codesh", None)
        if not hs:
            return Response({"error": "codesh manquant"}, status=400)

        valeurs = Valeur.objects.filter(codesh__icontains=hs)
        serializer = self.get_serializer(valeurs, many=True)
        return Response(serializer.data)

    # 🔥 Route personnalisée : upload d’image BLOB
    @action(detail=True, methods=["post"])
    def upload_image(self, request, pk=None):
        instance = self.get_object()
        file = request.FILES.get("image")

        if not file:
            return Response({"error": "Aucun fichier envoyé"}, status=400)

        instance.image = file.read()   # Stocker en BLOB
        instance.save()

        return Response({"message": "Image enregistrée"}, status=200)


# =============================
#  HISTORIQUE VALEUR
# =============================
class HistoriqueValeurViewSet(BaseViewSet):
    queryset = HistoriqueValeur.objects.all()
    serializer_class = HistoriqueValeurSerializer


# =============================
#  VALIDATION
# =============================
class ValidationViewSet(BaseViewSet):
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer

