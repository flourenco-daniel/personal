import requests
import json

access_token = ''

account_id = ''

url = f'https://graph.facebook.com/v20.0/act_{account_id}/ads'

parameters = {
    'access_token': access_token,
    'fields': 'id, name, adset_id, campaign_id'
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))   
else:
    print(f"Erro: {response.status_code}")
    print(response.text)
