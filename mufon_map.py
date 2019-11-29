import geopy.geocoders
from geopy.geocoders import Nominatim
import pandas as pd
import csv

df = pd.read_csv('ENV/mufon.csv')

geopy.geocoders.options.default_user_agent = 'mufon_map'
geopy.geocoders.options.default_timeout = 7
geolocator = Nominatim()
for row in df["Location"]:
    if geolocator.geocode(row):
        location = geolocator.geocode(row)
        with open('ENV/heatmap.csv', 'a') as fd:
            wr = csv.writer(fd)
            wr.writerow([row, location.latitude, location.longitude, 1])

df2 = pd.read_csv("ENV/heatmap.csv")

df2.drop(df2.columns.difference(['name', 'lat', 'lon', 'magnitude']), 1, inplace=True)
