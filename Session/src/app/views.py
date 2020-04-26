from django.shortcuts import render
from django.http import HttpResponse 
import requests
import json

# Create your views here.
def home(request):
    url = "https://covid19.mathdro.id/api"
    response = requests.get(url).json()

    res2 = requests.get("https://covid19.mathdro.id/api/countries").json()

    res2 = res2.get('countries','')

    countries =[]

    for i in res2:
           countries.append(i.get('name',''))
    daily = requests.get("https://covid19.mathdro.id/api/daily").json()

    con =[]
    det =[]
    date =[]

    for i in daily:
           con.append(i.get('confirmed','').get('total',''))
           det.append(i.get('deaths','').get('total',''))
           date.append(i.get('reportDate',''))
            
    context ={ 
       'confirmedCases':response.get('confirmed','').get('value',''), 
       'recoveredCases':response.get('recovered','').get('value',''),
       'deathcont':response.get('deaths','').get('value',''),
       'confirmed':con,
       'deaths':det,
       'date':date,
       'countries':countries,
       'bar':False,
       }
    return render(request,"app/index.html",context)

def countryData(request):
       if request.method == 'POST':
              country = request.POST['optional']
              response = requests.get('https://covid19.mathdro.id/api/countries/'+country).json()

              res2 =requests.get('https://covid19.mathdro.id/api/countries').json()

              res2 = res2.get('countries','')

              countries= []

              for i in res2:
                     countries.append(i.get('name',''))
             
              context = {
                  'confirmedCases':response.get('confirmed','').get('value',''),
                  'recoveredCases':response.get('recovered','').get('value',''),
                  'deathcont':response.get('deaths','').get('value',''),
                  'countries':countries,
                  'countryName':country,
                  'bar':True,
              }
              return render(request,"app/index.html",context)
       else:
           return HttpResponse("done")