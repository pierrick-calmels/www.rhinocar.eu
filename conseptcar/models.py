from django.db import models

# Create your models here.

class SondageParticulier(models.Model):
    age = models.CharField(max_length=200,default="unknown")
    temps_permis = models.CharField(max_length=200, default="unknown")
    profession = models.CharField(max_length=200,default="unknown")
    heure_depart = models.CharField(max_length=50, default="unknown")
    heure_retour = models.CharField(max_length=50, default="unknown")
    trois_huits =  models.CharField(max_length=50, default="unknown")
    zone_res =  models.CharField(max_length=50, default="unknown")
    lieu_travail =  models.CharField(max_length=50, default="unknown")
    transports =  models.CharField(max_length=50, default="unknown")
    temps_bouchons = models.CharField(max_length=50, default="unknown")
    freq_embout = models.CharField(max_length=50, default="unknown")
    deplacement = models.CharField(max_length=50, default="unknown")
    itineraire = models.CharField(max_length=50, default="unknown")
    moyen_transport = models.CharField(max_length=50, default="unknown")
    depense_annee = models.CharField(max_length=50, default="NSP")
    covoit = models.CharField(max_length=50, default="unknown")


    def __unicode__(self):
        return self.age
class Message(models.Model):
    name = models.CharField(max_length=200,default="unknown")
    email = models.EmailField(max_length=200,default="unknown")
    message = models.CharField(max_length=2000,default="unknown")

    def __unicode__(self):
        return self.email
