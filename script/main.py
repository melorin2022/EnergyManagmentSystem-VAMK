import time
import random
from energy_price import get_electricity_prices

# Constants
MAX_SOLAR_OUTPUT = 6  # in kW
BATTERY_CAPACITY = 10  # in kWh
LOW_BATTERY_THRESHOLD = 0.2  # 20% of battery capacity
HIGH_BATTERY_THRESHOLD = 0.8  # 80% of battery capacity
MIN_BATTERY_THRESHOLD = 0.1  # 10% of battery capacity for reserve
HIGH_SELL_PRICE_THRESHOLD = 0.15  # arbitrary value for high electricity price (€/kWh)
LOW_BUY_PRICE_THRESHOLD = 0.05  # arbitrary value for low electricity price (€/kWh)

# Function to simulate getting next hour data (can be replaced with API calls)
def get_next_hour_data():
    battery_level = random.uniform(0, 1)  # Battery charge as a percentage (0-1)
    solar_forecast = random.uniform(0, MAX_SOLAR_OUTPUT)  # Solar output in kW for next hour
    consumption_forecast = random.uniform(2, 5)  # Forecasted energy consumption (in kW)
    
    # electricity_price = random.uniform(0.03, 0.2)  # Electricity price per kWh
    electricity_prices = get_electricity_prices(next_hours=2)

    weather_forecast = random.choice(["sunny", "cloudy"])  # Random weather forecast
    return battery_level, solar_forecast, consumption_forecast, electricity_price, weather_forecast

# Decision-making function
def make_decision(battery_level, solar_forecast, consumption_forecast, electricity_price, weather_forecast):

    # Update solar output forecast based on weather
    if weather_forecast == "cloudy":
        solar_forecast *= 0.5  # Assume 50% reduction in solar output due to clouds

    # Scenario 1: If battery is not full and excess solar is available, store energy
    if solar_forecast > consumption_forecast and battery_level < 1:
        energy_to_store = min(solar_forecast - consumption_forecast, BATTERY_CAPACITY * (1 - battery_level))
        return f"Store {energy_to_store:.2f} kW in the battery"

    # Scenario 2: If battery is nearly full and electricity prices are high, sell excess energy
    if battery_level > HIGH_BATTERY_THRESHOLD and electricity_price > HIGH_SELL_PRICE_THRESHOLD:
        energy_to_sell = min(solar_forecast - consumption_forecast, BATTERY_CAPACITY * battery_level)
        return f"Sell {energy_to_sell:.2f} kW to the grid"

    # Scenario 3: If the battery is low and electricity prices are low, buy from grid
    if battery_level < LOW_BATTERY_THRESHOLD and electricity_price < LOW_BUY_PRICE_THRESHOLD:
        energy_to_buy = min(BATTERY_CAPACITY * (1 - battery_level), consumption_forecast)
        return f"Buy {energy_to_buy:.2f} kW from the grid to charge battery"

    # Scenario 4: If solar output is not enough to cover forecasted consumption, use battery
    if solar_forecast < consumption_forecast and battery_level > MIN_BATTERY_THRESHOLD:
        energy_from_battery = min(consumption_forecast - solar_forecast, BATTERY_CAPACITY * battery_level)
        return f"Use {energy_from_battery:.2f} kW from the battery to cover demand"

    # Scenario 5: If no action fits, maintain status quo
    return "No action, maintain current state"

# Main function to run hourly decision-making
def energy_management_system():
    while True:
        # Fetch the necessary data for the next hour
        battery_level, solar_forecast, consumption_forecast, electricity_price, weather_forecast = get_next_hour_data()
        
        # Print the fetched data for reference
        print(f"Battery Level: {battery_level:.2f} (max: 1.00), "
              f"Solar Forecast: {solar_forecast:.2f} kW, "
              f"Consumption Forecast: {consumption_forecast:.2f} kW, "
              f"Electricity Price: {electricity_price:.2f} €/kWh, "
              f"Weather: {weather_forecast}")

        # Make the decision for the next hour
        action = make_decision(battery_level, solar_forecast, consumption_forecast, electricity_price, weather_forecast)
        
        # Output the action
        print("Next hour action: ", action)
        
        # Wait for an hour (for simulation, we reduce it to 5 seconds here)
        time.sleep(5)  # change to `time.sleep(3600)` for actual hourly execution

# Run the energy management system
if __name__ == "__main__":
    energy_management_system()
