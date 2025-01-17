# EnergyManagmentSystem-VAMK
Globally, green energy sources are becoming very popular. Among the first places following this trend is Vaasa, Finland. Our project's main goal is to create an intelligent electrical battery so that people may utilize energy in their houses however they like. This approach will enable consumers to better control their power use, therefore lowering the household energy consumption. This is particularly relevant when running solar or other renewable energy source.

Using their transactions, we will examine consumer behavior on purchase, sale, and energy saving. By means of OpenMeteo's API, one may evaluate the possible solar energy production holistically, therefore enabling an analysis of the advantages and disadvantages of many energy sources. We will look at "Vaasan Sähkö's" real-time electricity expenses in search of best ways to save money.

The initiative seeks to provide Vaasa people with the information and tools required for sensible energy use. This will help the city to have a more safe and rich future.

Task distribution among our six-member project team has been efficient in ensuring the complete development of our smart electrical capacitor for Vaasa. GitHub has helped us to simplify our procedures. We have put our findings there for simple access. Should you find it interesting, you might get it from https://github.com/melorin2022/EnergyManagementSystem-VAMK.

# Task Design

## For meteorological data and documentation, how may APIs be applied? 
One group member is focused on compiling APIs especially "OpenMeteo" to provide exact meteorological data. This information is crucial in determining the amount of solar energy generated and the best time for capacitor charging.

Creating scenarios helps in decision-making: Another team member is creating scenarios that would help customers make wise decisions about their choices in other spheres as well as their energy buying, consuming, and selling. This will help local populations to better grasp the consequences of their activities in different environments.

## Real-time lighting evaluation
Two people share the task of coding the estimate of sunlight available at each one moment. Finding ideal charging times for the smart charger might help to maximize solar energy use.

## Examining energy usage
Examining patterns in energy use belongs to the duties of a team player. This research will enable individuals to maximize their energy consumption, therefore lowering expenses and improving the effectiveness of their operations.

## Creating a corporate strategy
Our main objective is to create a business strategy, defining our approach of presenting our solution to Vaasa's residents. This idea primarily aims to show how our smart capacitor may be integrated into the social energy ecosystem and its possible benefits for individuals.

By means of our combined efforts and individual expertise, we are sure that our program will provide a workable solution to enhance home energy management, therefore guiding Vaasa's future towards increased ecological sustainability.

# Solution Workflow

1. [x] Get Weather Forecasts from external APIs.
2. [ ] Predict Solar Energy Output.
3. [x] Predict Consumption.
4. [ ] Calculate remaining energy.
5. [x] Estimate peak hours for buying and selling.
6. [x] Make a decision to buy sell or store.

## Using AI

1. Energy management - buy, store or sell.
2. Energy demand forecasting using AI.
3. Integration with the inverter -> when to charge the battery or discharge.
   

# Sources
- Energy prices: [Spot Hinta](https://api.spot-hinta.fi)
- Weather Forecast: [Open Meteo](https://api.open-meteo.com/v1/forecast)
- Consumption in Finland: [Hourly Househol Enenrgy Consumption in Finland Jan - Dec. 2023](https://data.fingrid.fi/en/datasets/364)

# Cost Estimation
- Employee 6 , Salary per month =6*3000€ = 18000€
- Ec2= 2.77€/month
- VPS (4 threads, 50 GB storage, 10GB ram, 20€/month) = 100€

## Customers Cost Estimation
- Solar panel 6kw = 635€
- Power battery 10kw = 6500€

# Contributors
- Azar Kamali
- Shradha Shrestha
- Bindu Darlami Magar
- Kingsley Chima
- Md Hossain
- Amirhossein Mojiri Foroushani