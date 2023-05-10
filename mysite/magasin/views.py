from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProduitForm, FournisseurForm,UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

from rest_framework import viewsets
from magasin.models import Produit
from magasin.serializers import *

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
class ProduitNCViewSet(viewsets.ModelViewSet):
    queryset = ProduitNC.objects.all()
    serializer_class = ProduitNCSerializer
class ProduitCViewSet(viewsets.ModelViewSet):
    queryset = ProduitC.objects.all()
    serializer_class = ProduitCSerializer

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):  
    if request.user.is_superuser:
        return render( request,'adminpage.html')
    else:
        #request.session['username'] = request.user.username
        #logout(request)
        return render( request,'acceuil.html')
# Fourniseeeeeeeeeeeeeur
def FournisseurAdd(request):
    if request.method=="POST":
        form=FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/FournisseurShow')
    else:
        form=FournisseurForm()
    return render(request,'magasin/FournisseurAdd.html',{'form':form})
def FournisseurShow(request):
    Frs=Fournisseur.objects.all()
    return render(request,'magasin/FournisseurShow.html',{'Frs':Frs})
def FournisseurEdit(request,id):
    Frs=Fournisseur.objects.get(id=id)
    if (request.method == 'GET'):
        context = {'form': FournisseurForm(instance=Frs),'id':id}
        return render(request,'magasin/FournisseurEdit.html',context)
    if(request.method=='POST'):
        form=FournisseurForm(request.POST,instance=Frs)
        if(form.is_valid()):
            form.save()
            return redirect('/magasin')
    return render(request,'magasin/FournisseurEdit.html',{'form':form})
def FournisseurDestroy(request,id):
    Frs=Fournisseur.objects.get(id=id)
    Frs.delete()
    return HttpResponseRedirect('/magasin/FournisseurShow')

# Categorieeeeeeeeeeeeeeeeeeeeeeee
def CategorieAdd(request):
    if request.method=="POST":
        form=CategorieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/CategorieShow')
    else:
        form=CategorieForm()
    return render(request,'magasin/CategorieAdd.html',{'form':form})
def CategorieShow(request):
    Frs=Categorie.objects.all()
    return render(request,'magasin/CategorieShow.html',{'Frs':Frs})
def CategorieEdit(request,id):
    Frs=Categorie.objects.get(id=id)
    if (request.method == 'GET'):
        context = {'form': CategorieForm(instance=Frs),'id':id}
        return render(request,'magasin/CategorieEdit.html',context)
    if(request.method=='POST'):
        form=CategorieForm(request.POST,instance=Frs)
        if(form.is_valid()):
            form.save()
            return redirect('/magasin')
    return render(request,'magasin/CategorieEdit.html',{'form':form})
def CategorieDestroy(request,id):
    Frs=Categorie.objects.get(id=id)
    Frs.delete()
    return redirect('/magasin/CategorieShow')
# Produittttttttttttttt
def ProduitAdd(request):
    if request.method=="POST":
        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/ProduitShow')
    else:
        form=ProduitForm()
    return render(request,'magasin/ProduitAdd.html',{'form':form})
def ProduitShow(request):
    Frs=Produit.objects.all()
    return render(request,'magasin/ProduitShow.html',{'Frs':Frs})
def ProduitEdit(request,id):
    Frs=Produit.objects.get(id=id)
    if (request.method == 'GET'):
        context = {'form': ProduitForm(instance=Frs),'id':id}
        return render(request,'magasin/ProduitEdit.html',context)
    if(request.method=='POST'):
        form=ProduitForm(request.POST,instance=Frs).save()
        if(form.is_valid()):
            form.save()
            return redirect('/magasin')
    return render(request,'magasin/ProduitEdit.html',{'form':form})
def ProduitDestroy(request,id):
    Frs=Produit.objects.get(id=id)
    Frs.delete()
    return redirect('/magasin/ProduitShow')
# Produittttttttttttttt_CCCCCC
def ProduitCAdd(request):
    if request.method=="POST":
        form=ProduitCForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/ProduitCShow')
    else:
        form=ProduitCForm()
    return render(request,'magasin/ProduitCAdd.html',{'form':form})
def ProduitCShow(request):
    Frs=ProduitC.objects.all()
    return render(request,'magasin/ProduitCShow.html',{'Frs':Frs})
def ProduitCEdit(request,id):
    Frs=ProduitC.objects.get(id=id)
    if (request.method == 'GET'):
        context = {'form': ProduitCForm(instance=Frs),'id':id}
        return render(request,'magasin/ProduitCEdit.html',context)
    if(request.method=='POST'):
        form=ProduitCForm(request.POST,instance=Frs)
        if(form.is_valid()):
            form.save()
            return redirect('/magasin')
    return render(request,'magasin/ProduitCEdit.html',{'form':form})
def ProduitCDestroy(request,id):
    Frs=ProduitC.objects.get(id=id)
    Frs.delete()
    return redirect('/magasin/ProduitCShow')
# Produittttttttttttttt_NNNNNNNNNNCCCCCCCCC
def ProduitNCAdd(request):
    if request.method=="POST":
        form=ProduitNCForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/ProduitNCShow')
    else:
        form=ProduitNCForm()
    return render(request,'magasin/ProduitNCAdd.html',{'form':form})
def ProduitNCShow(request):
    Frs=ProduitNC.objects.all()
    return render(request,'magasin/ProduitNCShow.html',{'Frs':Frs})
def ProduitNCEdit(request,id):
    Frs=ProduitNC.objects.get(id=id)
    if (request.method == 'GET'):
        context = {'form': ProduitCForm(instance=Frs),'id':id}
        return render(request,'magasin/ProduitNCEdit.html',context)
    if(request.method=='POST'):
        form=ProduitNCForm(request.POST,instance=Frs)
        if(form.is_valid()):
            form.save()
            return redirect('/magasin')
    return render(request,'magasin/ProduitNCEdit.html',{'form':form})
def ProduitNCDestroy(request,id):
    Frs=ProduitNC.objects.get(id=id)
    Frs.delete()
    return redirect('/magasin/ProduitNCShow')
# Commandeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
def CommandeAdd(request):
    if request.method=="POST":
        form=CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/CommandeShow')
    else:
        form=CommandeForm()
    return render(request,'magasin/CommandeAdd.html',{'form':form})
def CommandeShow(request):
    Frs=Commande.objects.all()
    return render(request,'magasin/CommandeShow.html',{'Frs':Frs})
def CommandeEdit(request,id):
    Frs=Commande.objects.get(id=id)
    if (request.method == 'GET'):
        context = {'form': CommandeForm(instance=Frs),'id':id}
        return render(request,'magasin/CommandeEdit.html',context)
    if(request.method=='POST'):
        form=CommandeForm(request.POST,instance=Frs)
        if(form.is_valid()):
            form.save()
            return redirect('/magasin')
    return render(request,'magasin/CommandeEdit.html',{'form':form})
def CommandeDestroy(request,id):
    Frs=Commande.objects.get(id=id)
    Frs.delete()
    return redirect('/magasin/CommandeShow')
@login_required
def home(request):
    list=Produit.objects.all()
    return render(request,'acceuil.html',{'list':list})

def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('/magasin/ProduitShow')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})
#admin reset
from .forms import SetPasswordForm
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})


