from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import requests
import datetime
import pytz
from dotenv import load_dotenv
import os
load_dotenv()


def map_view(request):

  # map_url = "https://www.google.com/maps/embed/v1/view?key=AIzaSyCyU3I0Pkx7mcTZvj2YanFagPCygfNkI9E&center=40.730610,-73.935242"

  # if request.method == 'POST' and 'lat' in request.POST:
  #   lat = request.POST.get('lat')
  #   lng = request.POST.get('lng')
    
  #   # Do something with lat/lng
  #   return render(request, 'map.html', {'map_url': map_url})
  return render(request, 'map.html')

def get_weather(request):
  lat, lng = request.GET.get('lat'), request.GET.get('lng')
  API_KEY = os.environ.get('API_KEY')
  UNITS = "metric"
  exclude = "minutely"
  api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lng}&exclude={exclude}&appid={API_KEY}&units={UNITS}"
  response = requests.get(api_url)
  if response.status_code == 200:
    data = response.json()
  # timestamp = 1692719322
  # dt = datetime.datetime.utcfromtimestamp(timestamp)
  # dt = dt.replace(tzinfo=pytz.utc)

  # ist_tz = pytz.timezone('Asia/Kolkata')
  # dt = dt.astimezone(ist_tz)
  # https://codepen.io/ste-vg/pen/GqaZbo
  # https://gscode.in/css-weather-widget/
  # return JsonResponse(data)
  #print(data['hourly']- dt, temp, pressure, humidity, wind_speed, feels_like, wind_deg)
  return render(request, 'weather.html',{"hourly":data['hourly'], "current": data['current'], "lat": data.get('lat'), "lon": data.get('lon'), "today": data.get('daily')[0],"daily1": data.get('daily')[1:4], "daily2":data.get('daily')[4:], "alerts":data.get('alerts') })