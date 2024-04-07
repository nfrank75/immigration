from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def features(request):
    return render(request, 'features.html')

def formation(request):
    return render(request, 'formation.html')

def visa_affaire(request):
    return render(request, 'visa_affaire.html')

def visa_etude(request):
    return render(request, 'visa_etude.html')

def visa_touriste(request):
    return render(request, 'visa_touriste.html')

def visa_travailleur(request):
    return render(request, 'visa_travailleur.html')

def visa_asile(request):
    return render(request, 'visa_asile.html')

def confidentialite(request):
    return render(request, 'confidentialite.html.html')


def contact(request):
    if request.method == 'POST':
        # Traitement du formulaire
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pays = request.POST.get('country')
        message = request.POST.get('message')
        sujet = request.POST.get('sujet')

        contact = Contact(name=name, email=email, phone=phone, pays=pays, message=message, sujet=sujet)
        contact.save()
            
        # ...envoi d'un e-mail de notification

        # Redirigez l'utilisateur vers une page de succès ou affichez un message de succès
        # return render(request, 'success.html')
        # else:
        #     form = ContactForm()

    return render(request, 'contact.html')


def tcf_canada(request):
    return render(request, 'tcf_canada.html')
    
def tcf_quebec(request):
    return render(request, 'tcf_quebec.html')