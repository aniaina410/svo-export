from rest_framework import serializers
from .models import (
    Role, Direction, Service, Utilisateur,
    LogAction, ValeurExtrait, Valeur,
    HistoriqueValeur, Validation
)


# ---------------------
# ROLE
# ---------------------
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


# ---------------------
# DIRECTION
# ---------------------
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


# ---------------------
# SERVICE
# ---------------------
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


# ---------------------
# UTILISATEUR
# ---------------------
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


# ---------------------
# LOG ACTION
# ---------------------
class LogActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogAction
        fields = '__all__'


# ---------------------
# VALEUR EXTRAIT
# ---------------------
class ValeurExtraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValeurExtrait
        fields = '__all__'


# ---------------------
# VALEUR
# ---------------------
class ValeurSerializer(serializers.ModelSerializer):

    # Permet d’afficher l’image en base64
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return obj.image.hex()  # ou base64 si tu préfères plus tard
        return None

    class Meta:
        model = Valeur
        fields = '__all__'


# ---------------------
# HISTORIQUE VALEUR
# ---------------------
class HistoriqueValeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueValeur
        fields = '__all__'


# ---------------------
# VALIDATION
# ---------------------
class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = '__all__'
