from django.urls import path
from .import views

from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'magasin', ProduitViewSet)
router.register(r'categorie', CategorieViewSet)
router.register(r'commande', CommandeViewSet)
router.register(r'produitnc', ProduitNCViewSet)
router.register(r'produitc', ProduitCViewSet)
router.register(r'fournisseur', FournisseurViewSet)

urlpatterns=[
    path('API', include(router.urls)),
    path('',views.index),
    path('register/',views.register, name = 'register'),
    path('home/',views.home, name = 'home'),
    #Fournisseuuuuuur
    path('FournisseurAdd/',views.FournisseurAdd),
    path('FournisseurEdit/<int:id>/',views.FournisseurEdit,name='post-edit-f'),
    path('FournisseurDestroy/<int:id>/',views.FournisseurDestroy),
    path('FournisseurShow/',views.FournisseurShow),
    #Categorie
    path('CategorieAdd/',views.CategorieAdd),
    path('CategorieEdit/<int:id>/',views.CategorieEdit,name='post-edit-cat'),
    path('CategorieDestroy/<int:id>/',views.CategorieDestroy),
    path('CategorieShow/',views.CategorieShow),
    #Produit
    path('ProduitAdd/',views.ProduitAdd),
    path('ProduitEdit/<int:id>/',views.ProduitEdit,name='post-edit-p'),
    path('ProduitDestroy/<int:id>/',views.ProduitDestroy),
    path('ProduitShow/',views.ProduitShow),
    #ProduitNC
    path('ProduitNCAdd/',views.ProduitNCAdd),
    path('ProduitNCEdit/<int:id>/',views.ProduitNCEdit,name='post-edit-pnc'),
    path('ProduitNCDestroy/<int:id>/',views.ProduitNCDestroy),
    path('ProduitNCShow/',views.ProduitNCShow),
    #ProduitC
    path('ProduitCAdd/',views.ProduitCAdd),
    path('ProduitCEdit/<int:id>/',views.ProduitCEdit,name='post-edit-pc'),
    path('ProduitCDestroy/<int:id>/',views.ProduitCDestroy),
    path('ProduitCShow/',views.ProduitCShow),
    #Commande
    path('CommandeAdd/',views.CommandeAdd),
    path('CommandeEdit/<int:id>/',views.CommandeEdit,name='post-edit-cmd'),
    path('CommandeDestroy/<int:id>/',views.CommandeDestroy),
    path('CommandeShow/',views.CommandeShow),
    
    
]