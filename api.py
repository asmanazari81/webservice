
url = "https://dark-sky.p.rapidapi.com/%7Blatitude%7D,%7Blongitude%7D"

querystring = {"units":"auto","lang":"en"}

headers = {
  "X-RapidAPI-Key": "fa2ae83c39msh4ccfd5eeff89d1ep18ae3cjsnaed129db5729",
  "X-RapidAPI-Host": "dark-sky.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())