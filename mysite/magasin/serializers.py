from rest_framework import serializers
from .models import *

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'
class ProduitNCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduitNC
        fields = '__all__'
class ProduitCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduitC
        fields = '__all__'


