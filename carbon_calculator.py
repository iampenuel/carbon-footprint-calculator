# establish constants
co2_per_mile = 0.411  # kg/mile
co2_per_khw = 0.417  # kg/kWh
days_per_year = 365
months_per_year = 12
kg_to_ton = 1000

# define the function calculate_driving_emissions() with 'miles_per_day' as parameter
def calculate_driving_emissions(miles_per_day):
    # calculate driving emissions
    kg = miles_per_day * co2_per_mile * days_per_year
    # return driving emissions converted to ton
    return kg / kg_to_ton

# define the function calculate_electricity_emissions() with 'khw_per_month' as parameter
def calculate_electricity_emissions(kwh_per_month):
    # calculate electricity emissions
    kg = kwh_per_month * co2_per_khw * months_per_year
    # return electricity emissions converted to ton
    return kg / kg_to_ton

# define the 'main' function
def main():
    # create input for miles
    miles_per_day = float(input("Miles per day driven? "))
    # create input for kwh
    kwh_per_month = float(input("kWh per month used? "))
    gas = calculate_driving_emissions(miles_per_day)
    electricity = calculate_electricity_emissions(kwh_per_month)
    total = gas + electricity
    print(f"🚗 Driving: {gas:.2f} tons")
    print(f"💡 Electricity: {electricity:.2f} tons")
    print(f"🌍 Total: {total:.2f} tons")

main()



