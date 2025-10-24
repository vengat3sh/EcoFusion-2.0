def calculate_co2(energy_watts):
    energy_kwh = energy_watts / 1000
    emission_factor = 0.82  # kg CO₂ per kWh
    return round(energy_kwh * emission_factor, 3)
