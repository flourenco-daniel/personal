import requests
import csv

# Meta Ads API credentials
access_token = 'EAAUeZC6mFhnYBOyXmIDrbaRMfZChIFtDDhXWA8zqYafwlb0LywKfuGJ1eOjVeB1I1pmhVRG6ZCpZA04YzgFvFbw4LG3chE0i9twE3BKr7Y8xS0oCgAL6ewBdq5USZAlcJtZCnxgkxRO7KxUu21fZCTCPuWQXhjy2RyinIE68VMoTh04fxAkPnWaCpYXedaeeMTorfCqVUKxF3ZCi6C5UXFxHLisUFHrvUONVEWEZD'
account_id = '504914304557845'

# URL for the Meta Ads API insights endpoint
url = f'https://graph.facebook.com/v20.0/act_{account_id}/insights'

# Parameters for the report
parameters = {
    'access_token': access_token,
    'level': 'ad',  # You can change this to 'campaign' if you want campaign-level data
    'fields': 'campaign_name,adset_name,ad_name,date_start,date_stop,spend,impressions,clicks,actions',
    'time_increment': 1,
    'action_breakdowns': 'action_type',  # To get specific actions like App Installs, Register, etc.
}

# Request the report
response = requests.get(url, params=parameters)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()['data']  # Extract the data from the JSON response

    # Open a CSV file to write the data
    with open('meta_ads_all_period_report.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Campaign Name', 'Ad Set Name', 'Ad Name', 'Date Start', 'Date Stop', 'Spend', 'Impressions', 'Clicks', 'Action Type', 'Action Value'])

        # Write the rows
        for row in data:
            campaign_name = row.get('campaign_name', '')
            adset_name = row.get('adset_name', '')
            ad_name = row.get('ad_name', '')
            date_start = row.get('date_start', '')
            date_stop = row.get('date_stop', '')
            spend = row.get('spend', '')
            impressions = row.get('impressions', '')
            clicks = row.get('clicks', '')

            # Handle actions (like app installs, registrations, etc.)
            actions = row.get('actions', [])
            if actions:
                for action in actions:
                    action_type = action.get('action_type', '')
                    action_value = action.get('value', '')
                    writer.writerow([campaign_name, adset_name, ad_name, date_start, date_stop, spend, impressions, clicks, action_type, action_value])
            else:
                # If no actions, write a row without action data
                writer.writerow([campaign_name, adset_name, ad_name, date_start, date_stop, spend, impressions, clicks, '', ''])

    print("Meta Ads report for all period downloaded and formatted successfully.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")