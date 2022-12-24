import numpy as np
import random
import googlemaps
import requests
import json
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# AARNAV'S CODE:

def main(location):
    apikey = "AIzaSyDU4AHfNf3oACPsHYzSCqK6uEaxGF8Fr2I"
    gmaps = googlemaps.Client(key=apikey)
    namelist = []
    hourslist = []
    photolist = []
    ratinglist = []
    userratinglist = []
    typeslist = []
    vicinitylist = []
    reviewlist = []
    totaldifference = 0
    ans = []

    def matchLocations(name, place_id, totaldifference):
        payload = {}
        headers = {}
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + name + "&key=" + apikey
        jdata = json.loads(requests.request("GET", url, headers=headers, data=payload).text)
        if jdata["results"][0].get("name") == name and jdata["results"][0].get("place_id") != place_id:
            totaldifference += 1 
            return False

        else:
            return True

    def getLocations(url):
        print("blahhahahahha")
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        jdata = json.loads(response.text)
        countervar = 0

        while countervar <= len(list(jdata["results"])) - 1:        
            
            name = list(jdata["results"])[countervar].get("name")
            types = list(jdata["results"])[countervar].get("types")
            place_id = list(jdata["results"])[countervar].get("place_id")

            include = matchLocations(name, place_id, totaldifference)
            if include == True:
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
                    reviewlist.append(reviews[0].get("text") + reviews[1].get("text") + reviews[2].get("text"))
            else:
                print("removed", name)

            countervar += 1

    location = gmaps.geocode(location)[0] #like -33.8670522%2C151.1957362
    coords = str(location.get("geometry").get("bounds").get(("northeast")).get("lat")) + "%2C" + str(location.get("geometry").get("bounds").get(("northeast")).get("lng"))

    radius = "16000"
    type = 'restaurant'
    keyword = 'local'

    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + coords + "&radius=" + radius + "&type=" + type + "&keyword=" + keyword + "&key=" + apikey
    getLocations(url)

    headers = {}
    payload ={}
    response = requests.request("GET", url, headers=headers, data=payload)
    jdata = json.loads(response.text)

    if len(list(jdata["results"])) == 20 - totaldifference:
        print("second go:")
        url2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + coords + "&radius=" + radius + "&type=" + type + "&keyword=" + keyword + "&key=" + apikey + "&pagetoken=" + jdata.get("next_page_token")
        time.sleep(2)
        getLocations(url2)

    print(len(namelist))

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
                ans.pop(0)
                print(ans)
                
        get_recommendations(choice)
        dat = reviewlist
        name = namelist
        if len(name) != 0:
            choose = random.choice(name)
            print(choose)
            recommend(dat,name,choose)
        f = open("transfer.txt", "a")
        f.write(ans)
        f.close()

    print("END")
    file = open('data.txt','a+')
    file.writelines(ans)

main("pleasanton")