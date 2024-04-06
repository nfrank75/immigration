from django.urls import path
from .views import (home, about, contact, features, formation, visa_affaire,
                    visa_etude, visa_touriste, visa_travailleur, visa_asile, confidentialite)

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('features', features, name='features'),
    path('formation', formation, name='formation'),
    path('visa_affaire', visa_affaire, name='visa_affaire'),
    path('visa_etude', visa_etude, name='visa_etude'),
    path('visa_touriste', visa_touriste, name='visa_touriste'),
    path('visa_travailleur', visa_travailleur, name='visa_travailleur'),
    path('visa_asile', visa_asile, name='visa_asile'),
    path('confidentialite', confidentialite, name='confidentialite'),
]
