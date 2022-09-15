import requests
print(requests.__version__)

response = requests.get("https://raw.githubusercontent.com/Jasonchen-66/CMPUT455/master/version.py")
print(response.text)
