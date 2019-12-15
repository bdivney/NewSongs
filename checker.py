import requests
import urllib.parse
import json
import os
import datetime

d = datetime.datetime.today()
today = d.strftime('%Y-%m-%d')

urlAUTH = "https://accounts.spotify.com/api/token"
encodedToken = "Basic "
dataAUTH = {"grant_type":"client_credentials"}
headersAUTH = {"Authorization": encodedToken}

responseAUTH = requests.post(urlAUTH, headers = headersAUTH, data = dataAUTH)
responseAUTHData = responseAUTH.json()
accessToken = responseAUTHData["access_token"]
tokenType = responseAUTHData["token_type"]


for file in os.listdir("profiles/"):
	with open("profiles/" + file) as json_file:
		data = json.load(json_file)
		name = data["name"]
		for artist in data["artists"]:
			search = urllib.parse.quote(artist)
			urlNewReleases = "https://api.spotify.com/v1/search?q=" + search + "&type=album"
			headersNewReleases = {"Accept" : "application/json", "Authorization" : "Bearer " + accessToken, "Content-Type" : "application/json"}

			responseNewReleases = requests.get(url = urlNewReleases, headers = headersNewReleases)
			raw = responseNewReleases.json()
			for entry in raw["albums"]["items"]:
				if entry["release_date"] == today:
					print(entry["artists"][0]["name"] + " : " + entry["name"])
