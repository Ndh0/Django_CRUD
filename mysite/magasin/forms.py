from django.forms import ModelForm
from .models import *

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProduitForm(ModelForm): 
    class Meta : 
        model = Produit 
        fields = "__all__" #pour tous les champs de la table
class FournisseurForm(ModelForm): 
    class Meta : 
        model = Fournisseur 
        fields = "__all__"
class CategorieForm(ModelForm): 
    class Meta : 
        model = Categorie 
        fields = "__all__"
class ProduitCForm(ModelForm): 
    class Meta : 
        model = ProduitC
        fields = "__all__"
class ProduitNCForm(ModelForm): 
    class Meta : 
        model = ProduitNC 
        fields = "__all__"
class CommandeForm(ModelForm): 
    class Meta : 
        model = Commande 
        fields = "__all__"
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

from django.contrib.auth.forms import SetPasswordForm

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields