from django.db import models
from datetime import date

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return "\nNom : "+self.nom+"\nAdresse : "+self.adresse+"\nEmail : "+self.email+"\nTelephone : "+self.telephone+"\n"
class Categorie(models.Model):
    TYPE_CHOICES=[
        ('Al','Alimentaire'),
        ('Mb','Meuble'),
        ('Sn','Sanitaire'),
        ('Vs','Vaiselle'),
        ('Vt','Vetement'),
        ('Jx','Jouets'),
        ('Lg','Lige de Maison'),
        ('Bj','Bijoux'),
        ('Dc','Decor'),
    ]
    name=models.CharField(max_length=50,default='Al',choices=TYPE_CHOICES)
    
    def __str__(self):
        return "\nName : "+self.name+"\n"
class Produit(models.Model):
    TYPE_CHOICES=[
        ('em','Emballe'),
        ('fr','Frais'),
        ('cs','Conserve'),
    ]
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='Non define')
    prix=models.DecimalField(max_digits=20,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True,upload_to='media/')
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "\nLibelle : "+self.libelle+"\nDescription : "+self.description+"\nPrix : "+str(self.prix)+"\nType : "+self.type+"\n"
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return "\nLibelle : "+self.libelle+"\nDescription : "+self.description+"\nPrix : "+str(self.prix)+"\nType : "+self.type+"\nDuree Garantie : "+self.Duree_garantie+"\n"
class ProduitC(Produit):
    Duree_emb=models.CharField(max_length=100)
    def __str__(self):
        return "\nLibelle : "+self.libelle+"\nDescription : "+self.description+"\nPrix : "+str(self.prix)+"\nType : "+self.type+"\nDuree Emballage : "+self.Duree_garantie+"\n"
class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField(Produit)
    def __str__(self):
        return "\nDate Cde : "+str(self.dateCde)+"\nTotale : "+str(self.totalCde)+"\n"