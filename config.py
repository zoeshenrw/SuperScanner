from datetime import date, timedelta
from flask import Flask
import pymysql as sql
import pymysql.cursors
import geocoder as geo
global URL_info
global loc 
import math
import requests
# from register import register_bp

#Connecting to API
loc = geo.ip('me').latlng
URL_info = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae20295943'
   
#Connecting to the remote database
conn = sql.connect(host='sql.freedb.tech',
                   user='freedb_nyudb',
                   password='5?G3$vJ7c$8QSz4',
                   db='freedb_scannerdb',
                   unix_socket='',
                   charset='utf8mb4',
                   cursorclass=pymysql.cursors.DictCursor
                )

#Getting location.
geolocation = geo.ip('me')
   
#lat and long distance
def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

#get station information
def get_station_info(url, cur_loc):
   nearby_stations = []
   station_information = requests.get(url).json()['data']['stations']
   for station in station_information:
      station_name = station['name']
      station_lat = station['lat']
      station_lon = station['lon']
      station_capacity = station['capacity']
      if int(station_capacity)>=1 and distance(cur_loc, (station_lat, station_lon)) < 0.5:
         nearby_stations.append({"station_name":station_name,  "station_capacity":station_capacity, "station_lat":station_lat, "station_lon":station_lon})
   return nearby_stations

   