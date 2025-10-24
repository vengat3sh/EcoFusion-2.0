# ======================================================
# model.py — EcoFusion 2.0 (Full Multi-Device Component Mapping)
# ======================================================

import pandas as pd
import numpy as np


def load_dataset():
    data = {
        "Category": [
            "Air Conditioner", "Refrigerator", "Washing Machine", "Fan",
            "Television", "Computer", "Lighting", "Cooking Appliance"
        ],
        "Old_Component": [
            "Conventional AC", "Old Refrigerator", "Semi-Automatic Washing Machine",
            "Ceiling Fan", "CRT TV", "Desktop PC", "CFL Bulb", "Microwave Oven"
        ],
        "Modern_Component": [
            "Inverter AC", "Smart Refrigerator", "Front-Load Washing Machine",
            "BLDC Fan", "LED TV", "Laptop", "LED Bulb", "Induction Cooktop"
        ],
        "Updated_Component": [
            "AI Adaptive AC", "IoT Smart Refrigerator", "AI Sensor Washing Machine",
            "Smart IoT Fan", "Quantum Dot OLED TV", "AI Edge PC",
            "Smart Adaptive LED", "Smart Induction Hob"
        ],
        "Old_Energy(W)": [1800, 250, 500, 75, 120, 200, 20, 1200],
        "Modern_Energy(W)": [1200, 150, 300, 35, 60, 60, 9, 1800],
        "Updated_Energy(W)": [900, 120, 250, 25, 40, 45, 6, 1500],
        "Old_Eff(%)": [55, 40, 60, 70, 50, 45, 60, 60],
        "Modern_Eff(%)": [95, 75, 85, 92, 90, 80, 95, 90],
        "Updated_Eff(%)": [98, 90, 92, 96, 95, 90, 98, 95],
        "Old_Cost($)": [600, 200, 150, 40, 150, 800, 3, 100],
        "Modern_Cost($)": [800, 500, 300, 70, 300, 900, 5, 150],
        "Updated_Cost($)": [1000, 700, 450, 90, 500, 1200, 7, 200],
    }

    df = pd.DataFrame(data)
    df["CO2_Factor"] = 0.82
    df["Old_CO2(kg/hr)"] = (df["Old_Energy(W)"] / 1000) * df["CO2_Factor"]
    df["Modern_CO2(kg/hr)"] = (df["Modern_Energy(W)"] / 1000) * df["CO2_Factor"]
    df["Updated_CO2(kg/hr)"] = (df["Updated_Energy(W)"] / 1000) * df["CO2_Factor"]
    return df


def get_component_breakdown(category):
    """Return 10–12 component-level mappings for each appliance"""
    components = {
        "Air Conditioner": {
            "Old": {
                "Compressor": "Fixed-speed Rotary",
                "Condenser Coil": "Aluminium",
                "Refrigerant": "R22",
                "Filter": "Mesh Filter",
                "Sensor": "Mechanical Thermostat",
                "Motor": "AC Induction",
                "Controller": "Manual Knob",
                "Expansion Valve": "Capillary Tube",
                "Housing": "Basic Plastic",
                "Noise Level": "High",
            },
            "Modern": {
                "Compressor": "Inverter Rotary",
                "Condenser Coil": "Copper (Blue Fin)",
                "Refrigerant": "R32 Eco",
                "Filter": "PM2.5 Filter",
                "Sensor": "Digital Thermistor",
                "Motor": "BLDC",
                "Controller": "Digital Thermostat",
                "Expansion Valve": "Electronic",
                "Housing": "ABS Plastic",
                "Noise Level": "Low",
            },
            "Updated": {
                "Compressor": "AI Variable Scroll Compressor",
                "Condenser Coil": "Nano-Coated Copper",
                "Refrigerant": "R290 (Ultra-Low GWP)",
                "Filter": "HEPA + UV Sterilization",
                "Sensor": "IoT Smart Multi-Sensor",
                "Motor": "BLDC SmartSync",
                "Controller": "AI Adaptive Voice/App",
                "Expansion Valve": "Smart Proportional Valve",
                "Housing": "Recyclable Biopolymer",
                "Noise Level": "Whisper Mode",
                "Connectivity": "Wi-Fi + Cloud Learning",
                "Cooling Mode": "Self-Optimizing Adaptive Cooling",
            },
        },

        "Refrigerator": {
            "Old": {
                "Compressor": "Reciprocating",
                "Refrigerant": "R134a",
                "Coil": "Bare Metal",
                "Thermostat": "Manual Dial",
                "Lighting": "Incandescent Bulb",
                "Defrost": "Manual",
                "Shelves": "Plastic",
                "Door Seal": "Rubber",
                "Insulation": "PU Foam",
                "Motor": "Fixed Speed",
            },
            "Modern": {
                "Compressor": "Digital Inverter",
                "Refrigerant": "R600a",
                "Coil": "Aluminium Alloy",
                "Thermostat": "Electronic",
                "Lighting": "LED",
                "Defrost": "Auto",
                "Shelves": "Tempered Glass",
                "Door Seal": "Anti-bacterial",
                "Insulation": "High-Density Foam",
                "Motor": "Variable Speed",
            },
            "Updated": {
                "Compressor": "AI Linear Compressor",
                "Refrigerant": "R1234yf (Green Blend)",
                "Coil": "Graphene Alloy Coil",
                "Thermostat": "AI Predictive Control",
                "Lighting": "Smart Adaptive LED",
                "Defrost": "AI Auto Defrost",
                "Shelves": "Smart Weight Sensors",
                "Door Seal": "Self-Healing Magnetic Seal",
                "Insulation": "Vacuum Nano Insulation",
                "Motor": "EcoSynch Variable Drive",
                "Connectivity": "IoT + Inventory Tracking",
                "Control System": "App + Voice Integration",
            },
        },

        "Washing Machine": {
            "Old": {
                "Motor": "Belt-Driven AC Motor",
                "Drum": "Plastic",
                "Control": "Manual Knob",
                "Heater": "Fixed Resistive Coil",
                "Pump": "Fixed-Speed",
                "Sensor": "Mechanical Timer",
                "Panel": "Analog",
                "Drive Type": "Belt Drive",
                "Water Valve": "Basic Solenoid",
                "Body": "Plastic Frame",
            },
            "Modern": {
                "Motor": "Inverter Direct Drive",
                "Drum": "Steel Drum",
                "Control": "Digital Panel",
                "Heater": "Ceramic Heater",
                "Pump": "Variable-Speed",
                "Sensor": "Load Sensor",
                "Panel": "Touch Control",
                "Drive Type": "Direct Drive",
                "Water Valve": "Electronic",
                "Body": "Stainless Steel",
            },
            "Updated": {
                "Motor": "AI Direct Drive BLDC",
                "Drum": "NanoShield Stainless Steel",
                "Control": "AI Predictive Smart Panel",
                "Heater": "Self-Cleaning Ceramic",
                "Pump": "EcoSense Adaptive Flow",
                "Sensor": "AI Load + Dirt Sensors",
                "Panel": "Smart Touch + App",
                "Drive Type": "Sensorless Torque Control",
                "Water Valve": "Smart Flow Valve",
                "Body": "Recycled Polycomposite",
                "Connectivity": "IoT + Self Diagnostics",
                "Eco Wash": "Auto Optimize Water/Energy",
            },
        },

        "Fan": {
            "Old": {
                "Motor": "AC Induction",
                "Blade": "Metal",
                "Speed Control": "Manual Regulator",
                "Bearings": "Friction Bearings",
                "Body": "Iron",
                "Mounting": "Fixed Rod",
                "Power Supply": "AC 230V",
                "Protection": "Basic Grill",
                "Noise": "High",
                "Efficiency": "Low",
            },
            "Modern": {
                "Motor": "BLDC",
                "Blade": "Polymer",
                "Speed Control": "Remote",
                "Bearings": "Ball Bearings",
                "Body": "Plastic",
                "Mounting": "Adjustable Rod",
                "Power Supply": "DC Converter",
                "Protection": "Safety Grill",
                "Noise": "Low",
                "Efficiency": "High",
            },
            "Updated": {
                "Motor": "Smart BLDC IoT Motor",
                "Blade": "Carbon Fiber Aero Design",
                "Speed Control": "Smart Remote + App",
                "Bearings": "Sealed Ceramic Bearings",
                "Body": "Recyclable Alloy",
                "Mounting": "Smart Adjustable Mount",
                "Power Supply": "DC + Solar Backup",
                "Protection": "Smart Obstruction Sensor",
                "Noise": "Silent",
                "Efficiency": "Super High",
                "Sensors": "Temperature + Motion Sensors",
                "Connectivity": "IoT + Voice Command",
            },
        },

        "Television": {
            "Old": {
                "Display": "CRT",
                "Backlight": "Cathode Ray",
                "Resolution": "480p",
                "Panel Type": "Glass Tube",
                "Audio": "Mono",
                "Connectivity": "RF Only",
                "Frame": "Plastic",
                "Input": "AV Ports",
                "Energy": "High",
                "Color Depth": "Limited",
            },
            "Modern": {
                "Display": "LED",
                "Backlight": "Edge LED",
                "Resolution": "4K UHD",
                "Panel Type": "Flat Panel",
                "Audio": "Stereo",
                "Connectivity": "HDMI / USB",
                "Frame": "Metal",
                "Input": "Multiple Ports",
                "Energy": "Moderate",
                "Color Depth": "Wide Gamut",
            },
            "Updated": {
                "Display": "Quantum Dot OLED",
                "Backlight": "Self-Emissive",
                "Resolution": "8K Adaptive",
                "Panel Type": "Ultra Thin Flexible",
                "Audio": "Dolby Atmos AI Surround",
                "Connectivity": "Wi-Fi 6 / Bluetooth 5.3",
                "Frame": "Carbon Fiber Edge",
                "Input": "Wireless + HDMI 2.2",
                "Energy": "Optimized AI",
                "Color Depth": "1B+ Colors",
                "Processor": "Neural Image Processor",
                "Smart OS": "AI Vision Interface",
            },
        },

        "Computer": {
            "Old": {
                "CPU": "Intel Core 2 Duo",
                "Cooling": "Fan-based",
                "Power Supply": "400W ATX",
                "Storage": "HDD",
                "GPU": "Integrated Basic",
                "RAM": "DDR2",
                "Motherboard": "Non-Optimized PCB",
                "OS": "Legacy OS",
                "Connectivity": "Ethernet Only",
                "Case": "Steel Chassis",
            },
            "Modern": {
                "CPU": "i7 / Ryzen 7",
                "Cooling": "Heat Pipe + Fan",
                "Power Supply": "650W Modular",
                "Storage": "SSD",
                "GPU": "Dedicated",
                "RAM": "DDR4",
                "Motherboard": "Energy Efficient PCB",
                "OS": "Windows / Linux",
                "Connectivity": "Wi-Fi 6 + Bluetooth 5",
                "Case": "Aluminum",
            },
            "Updated": {
                "CPU": "AI Edge Processor (ARM + Neural Cores)",
                "Cooling": "Liquid + AI-Control",
                "Power Supply": "USB-C PD + Renewable Input",
                "Storage": "NVMe Gen5 SSD",
                "GPU": "Integrated Neural GPU",
                "RAM": "LPDDR5x Adaptive",
                "Motherboard": "Graphene-Based Eco Board",
                "OS": "Edge AI OS",
                "Connectivity": "Wi-Fi 7 + 6G Ready",
                "Case": "Recycled Carbon Fiber",
                "Sensors": "Thermal + Usage AI Sensors",
                "Cloud Sync": "Auto Backup + Optimization",
            },
        },

        "Lighting": {
            "Old": {
                "Type": "CFL",
                "Efficiency": "60 lm/W",
                "Base": "E27 Screw",
                "Driver": "Magnetic Ballast",
                "Color": "Warm White",
                "Material": "Glass",
                "Power": "High",
                "Life": "6,000 hrs",
                "Control": "Switch",
                "Heat": "Moderate",
            },
            "Modern": {
                "Type": "LED",
                "Efficiency": "110 lm/W",
                "Base": "B22 Bayonet",
                "Driver": "Electronic",
                "Color": "Cool White",
                "Material": "Plastic",
                "Power": "Low",
                "Life": "25,000 hrs",
                "Control": "Dimmable Switch",
                "Heat": "Low",
            },
            "Updated": {
                "Type": "Smart Adaptive LED",
                "Efficiency": "140 lm/W",
                "Base": "Smart Wireless Base",
                "Driver": "IoT Adaptive Driver",
                "Color": "Dynamic RGB + Circadian",
                "Material": "Recycled Polymer",
                "Power": "Ultra Low",
                "Life": "50,000 hrs",
                "Control": "App + Voice",
                "Heat": "Negligible",
                "Sensors": "Light + Occupancy Sensors",
                "Connectivity": "Wi-Fi + Cloud Sync",
            },
        },

        "Cooking Appliance": {
            "Old": {
                "Heating": "Convection Coil",
                "Surface": "Metal",
                "Control": "Knob",
                "Safety": "Thermal Fuse",
                "Material": "Steel",
                "Timer": "Manual",
                "Sensor": "None",
                "Power": "High",
                "Body": "Plastic Frame",
                "Efficiency": "Low",
            },
            "Modern": {
                "Heating": "Induction",
                "Surface": "Ceramic",
                "Control": "Touch",
                "Safety": "Auto Shutoff",
                "Material": "Glass",
                "Timer": "Digital",
                "Sensor": "Temperature Sensor",
                "Power": "Moderate",
                "Body": "Steel + Glass",
                "Efficiency": "High",
            },
            "Updated": {
                "Heating": "AI Induction Magnetic Field",
                "Surface": "Nano-Coated Ceramic",
                "Control": "Smart Touch + App",
                "Safety": "AI Auto Detection",
                "Material": "Recycled Glass Ceramic",
                "Timer": "Adaptive Predictive",
                "Sensor": "Smart Cooking Sensors",
                "Power": "Auto Adjust",
                "Body": "Eco Alloy Frame",
                "Efficiency": "Ultra High",
                "Connectivity": "IoT Cloud Recipes",
                "Assistant": "Voice Cooking Guide",
            },
        },
    }

    return components.get(category, None)


def analyze_efficiency(category, hours_per_day, electricity_rate):
    df = load_dataset()
    row = df[df["Category"] == category].iloc[0]

    energy_diff = row["Old_Energy(W)"] - row["Updated_Energy(W)"]
    co2_diff = row["Old_CO2(kg/hr)"] - row["Updated_CO2(kg/hr)"]
    eff_gain = row["Updated_Eff(%)"] - row["Old_Eff(%)"]

    annual_hours = hours_per_day * 365
    annual_energy_saved = (energy_diff / 1000) * annual_hours
    annual_co2_saved = co2_diff * annual_hours
    annual_cost_saved = annual_energy_saved * electricity_rate

    summary = {
        "category": category,
        "old": row["Old_Component"],
        "modern": row["Modern_Component"],
        "updated": row["Updated_Component"],
        "energy_diff": energy_diff,
        "co2_diff": co2_diff,
        "eff_gain": eff_gain,
        "annual_energy_saved": annual_energy_saved,
        "annual_co2_saved": annual_co2_saved,
        "annual_cost_saved": annual_cost_saved,
        "old_row": row,
        "components": get_component_breakdown(category),
    }

    return summary
