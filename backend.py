import numpy as np
import random
import googlemaps
import requests
import json
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# AARNAV'S CODE:

apikey = "AIzaSyBLC-qqM7M1Y9JIoJKbijKmHVD04Z4x9Mk"
gmaps = googlemaps.Client(key=apikey)
namelist = []
hourslist = []
photolist = []
ratinglist = []
userratinglist = []
typeslist = []
vicinitylist = []
reviewlist = []

def getLocations(url):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    jdata = json.loads(response.text)
    countervar = 0

    while countervar <= len(list(jdata["results"])) - 1:        
        
        name = list(jdata["results"])[countervar].get("name")
        types = list(jdata["results"])[countervar].get("types")

        namelist.append(name)
        hourslist.append(list(jdata["results"])[countervar].get("opening_hours"))
        photolist.append(list(jdata["results"])[countervar].get("photos"))
        ratinglist.append(list(jdata["results"])[countervar].get("rating"))
        userratinglist.append(list(jdata["results"])[countervar].get("user_ratings_total"))
        typeslist.append(types)
        vicinitylist.append(list(jdata["results"])[countervar].get("vicinity"))

        url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=" + list(jdata["results"])[countervar].get("place_id") + "&fields=name,rating,formatted_phone_number,reviews&key=" + apikey
        payload={}
        headers = {}
        if len(json.loads(requests.request("GET", url, headers=headers, data=payload).text)["result"]) == 4:
            reviews = list(json.loads(requests.request("GET", url, headers=headers, data=payload).text)['result'].get("reviews"))
            reviewlist.append(reviews[0].get("text"))

        countervar += 1

location = gmaps.geocode(input("city:\n\t"))[0] #like -33.8670522%2C151.1957362
coords = str(location.get("geometry").get("bounds").get(("northeast")).get("lat")) + "%2C" + str(location.get("geometry").get("bounds").get(("northeast")).get("lng"))

radius = "16000"
type = input("what type of business?\n\t")
keyword = input("keywords:\n\t")

url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + coords + "&radius=" + radius + "&type=" + type + "&keyword=" + keyword + "&key=" + apikey
getLocations(url)

headers = {}
payload ={}
response = requests.request("GET", url, headers=headers, data=payload)
jdata = json.loads(response.text)

if len(list(jdata["results"])) == 20:
    url2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + coords + "&radius=" + radius + "&type=" + type + "&keyword=" + keyword + "&key=" + apikey + "&pagetoken=" + jdata.get("next_page_token")
    time.sleep(1)
    getLocations(url2)


# ANISH'S CODE:
def recommend(data,names,choice):
 vector = TfidfVectorizer(stop_words='english')
 vec_matrix = vector.fit_transform(data)
 #finds fetaures in the text
 vector.get_feature_names_out()[5000:5010]
 #finds cosine similarity between features
 cosine = linear_kernel(vec_matrix, vec_matrix)
 def get_recommendations(title, cosine=cosine):
      duf = names.index(title)
      jow = cosine[duf]
      ans =[]
      jow = list(jow)
      for i in jow:
         if i > 0:
             joa = jow.index(i)
             ans.append(names[joa])
      ans.remove(title)
      #incase no similarty is found
      if ans == []:
           print(random.choice(names))
      else:
           print(ans[0])
           
 get_recommendations(choice)
dat = reviewlist
name = namelist
choose = random.choice(name)
recommend(dat,name,choose)