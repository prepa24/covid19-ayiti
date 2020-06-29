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
	url = "https://bet365-scoccer-odds.p.rapidapi.com/v1/league"
	querystring = {"sport_id":"38"}
	
	headers = {
    'x-rapidapi-host': "chile-coronapi1.p.rapidapi.com",
    'x-rapidapi-key': "d654c6e88bmsh8541e40f51428dfp1e41d3jsnf7f7df62b51c"
    }
	
	response = requests.get(url, headers=headers, params=querystring)
	data = response.json()
	print(data)

	return render(request,'kantite/chile.html', {
		
        
		})

def about(request):
	context={
		    'titre':'Covid-19 Ayiti'
		}
	
	return render(request,'kantite/about.html',context)