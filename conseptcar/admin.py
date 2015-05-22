from django.contrib import admin
from conseptcar.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class ParticulierResource(resources.ModelResource):

    class Meta:
        model = SondageParticulier
        fields = ('age', 'temps_permis', 'profession', 'heure_depart', 'heure_retour', 'trois_huits', 'zone_res', 'lieu_travail', 'transports', 'temps_bouchons',
        'freq_embout',
        'deplacement',
        'itineraire',
        'moyen_transport',
        'depense_annee',
        'covoit')

class ParticuliersAdmin(ImportExportModelAdmin):
    resource_class = ParticulierResource
    pass

class MessageResource(resources.ModelResource):

    class Meta:
        model = Message
        fields = ('name', 'email', 'message')

class MessageAdmin(ImportExportModelAdmin):
    resource_class = MessageResource
    pass




# Register your models here.
admin.site.register(SondageParticulier, ParticuliersAdmin)
admin.site.register(Message, MessageAdmin)
