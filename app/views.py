from django.shortcuts import render
import json
import urllib.request


#api: 6a56894c7c20a1992479a61a5ea3b144
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=6a56894c7c20a1992479a61a5ea3b144').read()
            json_data = json.loads(res)
            weather = {
                'city': json_data['name'],
                'country_code': str(json_data['sys']['country']),
                'cordinate': str(json_data['coord']['lon'])+','+str(json_data['coord']['lat']),
                'temp': str(json_data['main']['temp'])+'k',
                'pressure': str(json_data['main']['pressure']),
                'humidity': str(json_data['main']['humidity']),
                'wind': str(json_data['wind']['speed']),
                'clouds': str(json_data['clouds']['all']),
            }    
            return render(request, 'index.html', {'weather': weather})
        except:
            return render(request, 'index.html', {'erreur': 'invalid city'})
    else:
        weather = {}
        return render(request, 'index.html')
 