import requests

def get_electricity_price(next_hour=1):
    base_url = "https://api.spot-hinta.fi"

    # Fetch data for the next few hours
    url = f"{base_url}/JustNow?lookForwardHours={next_hour}&isHtmlRequest=true"
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()
        # Extract the relevant information
        price_with_tax = data['PriceWithTax']
    else:
        print(f"Failed to fetch data for hour {i}, status code: {response.status_code}")
    
    return price_with_tax
