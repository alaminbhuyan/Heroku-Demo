import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'speed':150, 'car_age':5, 'experience':6})

print(r.json())