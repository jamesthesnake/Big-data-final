import requests

def get_polling_data(race):
    api_url = f"https://api.realclearpolitics.com/v1/polls/?race={race}"
    headers = {'User-Agent': 'Your-App-Name'}
    
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Extract relevant polling data
        polling_data = []
        for poll in data['polls']:
            poll_data = {
                'pollster': poll['pollster'],
                'date': poll['date'],
                'sample_size': poll['sampleSize'],
                'margin_of_error': poll['marginError'],
                'results': poll['results']
            }
            polling_data.append(poll_data)
        
        return polling_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching polling data: {e}")
        return None

# Example usage: Get polling data for the 2024 Presidential Election
presidential_polls = get_polling_data("2024-presidential")
if presidential_polls:
    print("Polling Data for 2024 Presidential Election:")
    for poll in presidential_polls:
        print(f"Pollster: {poll['pollster']}")
        print(f"Date: {poll['date']}")
        print(f"Sample Size: {poll['sample_size']}")
        print(f"Margin of Error: {poll['margin_of_error']}")
        print("Results:")
        for candidate in poll['results']:
            print(f"{candidate['candidate']}: {candidate['value']}%")
        print("\n")
