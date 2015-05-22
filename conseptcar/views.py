from django.shortcuts import render
from conseptcar.models import *
from django.http import *

# Create your views here.
def index(request):

	return render(request, "index.html")

# test information page
def sondageParticulierForm(request):
	if request.method == 'GET':
		return render(request, "index.html")

	else :

		age 		   = request.POST['part-radio']
		temps_permis   = request.POST['part-radio1']
		profession     = request.POST.get("profession",None)
		heure_depart   = request.POST['part-radio3']
		heure_retour   = request.POST['part-radio4']
		trois_huits    = request.POST['part-radio5']
		zone_res       = request.POST['part-radio6']
		lieu_travail   = request.POST['part-radio7']
		transports     = request.POST['part-radio8']
		temps_bouchons = request.POST['part-radio9']
		freq_embout = request.POST['part-radio10']
		deplacement = request.POST['part-radio11']
		itineraire = request.POST['part-radio12']
		moyen_transport = request.POST['part-radio13']
		depense_annee = request.POST['part-radio15']
		covoit = request.POST['part-radio14']

		p = SondageParticulier(age = age,temps_permis = temps_permis,profession = profession,
		heure_depart = heure_depart,
		heure_retour = heure_retour,
		trois_huits = trois_huits,
		zone_res = zone_res,
		lieu_travail = lieu_travail,
		transports = transports,
		temps_bouchons = temps_bouchons,
		freq_embout = freq_embout,
		deplacement = deplacement,
		itineraire = itineraire,
		moyen_transport = moyen_transport,
		depense_annee = depense_annee,
		covoit = covoit)
		p.save()

		return HttpResponseRedirect("/home")

# Message

def messageForm(request):
	if request.method == 'GET':
		return render(request, "index.html")

	else :
		if(request.method == 'POST["Send Message"]') :
			name		   = request.POST['name']
			email   = request.POST['email']
			message     = request.POST['message']

			m = Message(name = name, email = email, message = message)
			m.save()

		return HttpResponseRedirect("/home")
