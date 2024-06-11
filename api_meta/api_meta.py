import requests
import json

access_token = 'EAAUeZC6mFhnYBOysyZALP8ZCKWjfzrvVnnU8ET6xcQaZBllHIkdvVjlXL1arNWYdDT8qaEm9x1WWX48auHuGow53cfSBZCBsgZCaFcAw6F7UM8gS5wFFMeqoBmTQ7Tn5I1REICPFLIG30KoWCqMDrllfEAOGCgHVDnrsT7IlhVmqXtJIDVp392EyCyqsinhJBEc7soJ5xuiycVIliB7Sa6yKj7ggZAZCHSF6MjYZD'

account_id = '170578383605870'

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