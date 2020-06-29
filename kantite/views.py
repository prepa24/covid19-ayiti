from django.shortcuts import render
import requests

# Create your views here.
def home(request):
	response = requests.get('https://corona.lmao.ninja/v2/countries/Haiti')
	geodata = response.json()
	
	return render(request,'kantite/home.html', {
		'countryInfo': geodata['countryInfo'],
        'country': geodata['country'],
        'cases': geodata['cases'],
        'todayCases': geodata['todayCases'],
        'tests': geodata['tests'],
        'recovered': geodata['recovered'],
        'active': geodata['active'],
        'critical': geodata['critical'],
        'deaths': geodata['deaths'],
        #pati jodia
        'todayRecovered': geodata['todayRecovered'],
        'todayDeaths': geodata['todayDeaths'],
        'critical': geodata['critical'],

		})

def chile(request):
	

	return render(request,'kantite/chile.html', )

def about(request):
	context={
		    'titre':'Covid-19 Ayiti'
		}
	
	return render(request,'kantite/about.html',context)