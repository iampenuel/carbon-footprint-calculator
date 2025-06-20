import streamlit as st

# Constants
co2_per_mile = 0.411  # kg/mile
co2_per_kwh = 0.417  # kg/kWh
days_per_year = 365
months_per_year = 12
kg_to_ton = 1000

# Function to calculate driving emissions
def calculate_driving_emissions(miles_per_day):
    kg = miles_per_day * co2_per_mile * days_per_year
    return kg / kg_to_ton

# Function to calculate electricity emissions
def calculate_electricity_emissions(kwh_per_month):
    kg = kwh_per_month * co2_per_kwh * months_per_year
    return kg / kg_to_ton

# Streamlit App Interface
def main():
    st.title("🌱 Carbon Footprint Tracker")
    st.write("Estimate your annual CO₂ emissions from daily driving and electricity use.")

    # Inputs
    miles_per_day = st.number_input("🚗 Miles driven per day:", min_value=0.0)
    kwh_per_month = st.number_input("💡 Electricity used per month (kWh):", min_value=0.0)

    if miles_per_day or kwh_per_month:
        gas = calculate_driving_emissions(miles_per_day)
        electricity = calculate_electricity_emissions(kwh_per_month)
        total = gas + electricity

        # Output
        st.markdown(f"### Results")
        st.success(f"🚗 **Driving CO₂: ** {gas:.2f} tons/year")
        st.info(f"💡 **Electricity CO₂: ** {electricity:.2f} tons/year")
        st.warning(f"🌍 **Total Annual Footprint: ** {total:.2f} tons")

if __name__ == "__main__":
    main()
