import requests

def get_electricity_prices(next_hours=2):
    base_url = "https://api.spot-hinta.fi"
    prices = []  # List to store the data for the next hours

    # Fetch data for the next few hours
    for i in range(next_hours + 1):
        url = f"{base_url}/JustNow?lookForwardHours={i}&isHtmlRequest=true"
        response = requests.get(url)
        
        if response.status_code == 200:  # Check if the request was successful
            data = response.json()
            # Extract the relevant information
            price_with_tax = data['PriceWithTax']
            
            # Append the price_with_tax to the list
            prices.append(price_with_tax)
        else:
            print(f"Failed to fetch data for hour {i}, status code: {response.status_code}")
    
    return prices  # Return the list of electricity prices
