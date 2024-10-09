import requests
import json

access_token = ''

account_id = ''

url = f'https://graph.facebook.com/v20.0/act_{account_id}/insights'

parameters = {
    'access_token': access_token,
    'level': 'ad',
    'fields': 'ad_id, spend, clicks, impressions, actions, action_values',
    'date_preset': 'last_30d',
    'limit': 1000
}

def get_purchases(actions):
    if actions:
        for action in actions:
            if action['action_type'] == 'purchase':
                return action['value']
    return 0

def get_purchase_value(action_values):
    if action_values:
        for action_value in action_values:
            if action_value['action_type'] == 'omni_purchase':
                return action_value['value']
    return 0.0


def filter_actions(actions):
    return [action for action in actions if action['action_type'] == 'purchase']

def filter_action_values(action_values):
    return [action_value for action_value in action_values if action_value['action_type'] == 'omni_purchase']

all_insights = []

while True:
    response = requests.get(url, params=parameters)
    if response.status_code == 200:
        data = response.json().get('data', [])
        
        for insight in data:
            insight['actions'] = filter_actions(insight.get('actions', []))
            insight['action_values'] = filter_action_values(insight.get('action_values', []))
            purchases = get_purchases(insight['actions'])
            purchase_value = get_purchase_value(insight['action_values'])
            insight['purchases'] = purchases
            insight['purchase_value'] = purchase_value
            all_insights.append(insight)    
        next_page = response.json().get('paging', {}).get('next')
        if next_page:
            url = next_page
        else:
            break
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        break

print(json.dumps(all_insights, indent=4))
