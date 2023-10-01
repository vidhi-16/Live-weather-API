import datetime
import pytz
from django import template
import reverse_geocoder as rg

register = template.Library()

@register.filter
def timestamp_to_ist(timestamp):

    dt = datetime.datetime.utcfromtimestamp(timestamp)
    dt = dt.replace(tzinfo=pytz.utc)
    ist_tz = pytz.timezone('Asia/Kolkata')
    dt = dt.astimezone(ist_tz)
    return dt

# {% load custom_filters %}

# {{ timestamp|timestamp_to_ist }}

@register.filter
def reverse_geocode(lat, lon):
    coordinates = (lat, lon)
    result = rg.search(coordinates)
    # [{'lat': '23.02579', 'lon': '72.58727', 'name': 'Ahmedabad', 'admin1': 'Gujarat', 'admin2': 'Ahmadabad', 'cc': 'IN'}]
    return f"{result[0].get('name')}, {result[0].get('admin1')} - {result[0].get('cc')}"