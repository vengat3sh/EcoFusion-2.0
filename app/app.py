# ======================================================
# app.py — EcoFusion 2.0 Streamlit Dashboard (Green-Themed Edition)
# ======================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import load_dataset, analyze_efficiency

# ------------------------------------------------------
# Streamlit Page Config
# ------------------------------------------------------
st.set_page_config(
    page_title="🌿 EcoFusion 2.0 – Smart Energy Framework",
    layout="wide",
    page_icon="🌱"
)

# ------------------------------------------------------
# Header
# ------------------------------------------------------
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.2em;
        color: #2E7D32;
        font-weight: 700;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #388E3C;
        margin-bottom: 1.5em;
    }
    .metric-card {
        background-color: #E8F5E9;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        box-shadow: 0px 0px 8px rgba(46,125,50,0.2);
    }
    .metric-value {
        font-size: 1.4em;
        font-weight: 700;
        color: #1B5E20;
    }
    .metric-label {
        color: #388E3C;
        font-size: 0.9em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-title'>🌿 EcoFusion 2.0</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Sustainable Intelligence Framework for Appliance Efficiency & CO₂ Optimization</div>", unsafe_allow_html=True)

df = load_dataset()

# ------------------------------------------------------
# Sidebar Controls
# ------------------------------------------------------
st.sidebar.header("⚙️ Configuration Panel")
category = st.sidebar.selectbox("Select Appliance Category", df["Category"].tolist())
hours_per_day = st.sidebar.slider("Average Usage Hours per Day", 1, 24, 6)
electricity_rate = st.sidebar.slider("Electricity Rate (₹ per kWh)", 3, 15, 7)

# ------------------------------------------------------
# Data Analysis
# ------------------------------------------------------
summary = analyze_efficiency(category, hours_per_day, electricity_rate)
row = summary["old_row"]

# ------------------------------------------------------
# Metric Cards
# ------------------------------------------------------
st.subheader(f"📊 {category} Energy & CO₂ Efficiency Summary")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(
    f"<div class='metric-card'><div class='metric-value'>{summary['energy_diff']:.1f} W/hr</div>"
    f"<div class='metric-label'>⚡ Energy Reduction</div></div>", unsafe_allow_html=True)
col2.markdown(
    f"<div class='metric-card'><div class='metric-value'>{summary['co2_diff']:.3f} kg/hr</div>"
    f"<div class='metric-label'>🌫 CO₂ Reduction</div></div>", unsafe_allow_html=True)
col3.markdown(
    f"<div class='metric-card'><div class='metric-value'>+{summary['eff_gain']:.1f}%</div>"
    f"<div class='metric-label'>⚙️ Efficiency Gain</div></div>", unsafe_allow_html=True)
col4.markdown(
    f"<div class='metric-card'><div class='metric-value'>₹{summary['annual_cost_saved']:.1f}/yr</div>"
    f"<div class='metric-label'>💰 Annual Cost Saved</div></div>", unsafe_allow_html=True)

st.markdown("---")

# ------------------------------------------------------
# Component Comparison Table
# ------------------------------------------------------
st.subheader("🔧 Component Evolution: Legacy → Modern → Self-Upgrading")

components = summary["components"]
if components:
    # Align component lengths safely
    all_keys = set(components["Old"].keys()) | set(components["Modern"].keys()) | set(components["Updated"].keys())

    def get_value(dic, key): return dic.get(key, "")
    comp_data = {
        "Component": list(all_keys),
        "Legacy": [get_value(components["Old"], k) for k in all_keys],
        "Modern": [get_value(components["Modern"], k) for k in all_keys],
        "Updated (Self-Upgrading)": [get_value(components["Updated"], k) for k in all_keys],
    }
    comp_df = pd.DataFrame(comp_data)
    st.dataframe(comp_df, use_container_width=True, hide_index=True)
else:
    st.info("Component details unavailable for this category.")

st.markdown("---")

# ------------------------------------------------------
# Charts Section
# ------------------------------------------------------
st.markdown("### 📈 Comparative Performance Visualization")

col1, col2, col3 = st.columns(3)
with col1:
    fig, ax = plt.subplots(figsize=(3.5, 2.5))
    ax.bar(["Legacy", "Modern", "Updated"],
           [row["Old_CO2(kg/hr)"], row["Modern_CO2(kg/hr)"], row["Updated_CO2(kg/hr)"]],
           color=["#e74c3c", "#f1c40f", "#2ecc71"])
    ax.set_title("CO₂ Emission (kg/hr)")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(3.5, 2.5))
    ax.bar(["Legacy", "Modern", "Updated"],
           [row["Old_Energy(W)"], row["Modern_Energy(W)"], row["Updated_Energy(W)"]],
           color=["#ff7043", "#fbc02d", "#66bb6a"])
    ax.set_title("Energy Consumption (W)")
    st.pyplot(fig)

with col3:
    fig, ax = plt.subplots(figsize=(3.5, 2.5))
    ax.bar(["Legacy", "Modern", "Updated"],
           [row["Old_Eff(%)"], row["Modern_Eff(%)"], row["Updated_Eff(%)"]],
           color=["#ef5350", "#fdd835", "#43a047"])
    ax.set_title("Efficiency (%)")
    st.pyplot(fig)

# ------------------------------------------------------
# Radar Chart — Multi-Factor Comparison
# ------------------------------------------------------
st.markdown("### 🕸️ Multi-Factor Performance Radar")

metrics = ["Efficiency", "CO₂ (low=better)", "Energy (low=better)", "Cost"]
old_vals = [row["Old_Eff(%)"], row["Old_CO2(kg/hr)"]*100, row["Old_Energy(W)"]/10, row["Old_Cost($)"]/10]
modern_vals = [row["Modern_Eff(%)"], row["Modern_CO2(kg/hr)"]*100, row["Modern_Energy(W)"]/10, row["Modern_Cost($)"]/10]
updated_vals = [row["Updated_Eff(%)"], row["Updated_CO2(kg/hr)"]*100, row["Updated_Energy(W)"]/10, row["Updated_Cost($)"]/10]

# Close radar loop
old_vals += old_vals[:1]
modern_vals += modern_vals[:1]
updated_vals += updated_vals[:1]
angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
angles += angles[:1]

fig2 = plt.figure(figsize=(5, 5))
ax2 = plt.subplot(111, polar=True)
ax2.plot(angles, old_vals, 'r-', linewidth=2, label='Legacy')
ax2.fill(angles, old_vals, 'r', alpha=0.25)
ax2.plot(angles, modern_vals, 'y-', linewidth=2, label='Modern')
ax2.fill(angles, modern_vals, 'y', alpha=0.25)
ax2.plot(angles, updated_vals, 'g-', linewidth=2, label='Updated')
ax2.fill(angles, updated_vals, 'g', alpha=0.25)
ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(metrics)
ax2.set_title(f"{category} – Multi-Factor Radar", color="#1B5E20", fontsize=11)
ax2.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))
st.pyplot(fig2)

# ------------------------------------------------------
# Recommendation Engine
# ------------------------------------------------------
st.markdown("### 🏆 Smart Upgrade Recommendation")

eco_score = (summary["eff_gain"] * 3) + (summary["annual_co2_saved"] / 10) + (summary["annual_cost_saved"] / 100)

if eco_score > 120:
    st.success(f"✅ **{summary['updated']}** is the optimal next-gen upgrade for your {category}.")
elif eco_score > 80:
    st.info(f"🟡 **{summary['modern']}** provides balanced efficiency and affordability.")
else:
    st.warning(f"⚠️ Continue with the **{summary['old']}** until newer models become viable.")

# ------------------------------------------------------
# Footer
# ------------------------------------------------------
st.markdown("---")
st.caption("© EcoFusion 2.0 | Sustainable Intelligence Framework | Developed for IBM Z Datathon 🌱")
