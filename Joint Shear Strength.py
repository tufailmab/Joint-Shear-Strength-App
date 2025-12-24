# Joint Shear Strength-App: Interactive Streamlit calculator for V_proposed using calibrated shear equation.

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ===========================
# Page configuration
# ===========================
st.set_page_config(
    page_title="Joint Shear Strength-App",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Joint Shear Strength Calculator")
st.markdown("""
This app computes the **predicted joint shear** \(V_{proposed}\) using the calibrated equation:

$$
V_{proposed} = C \cdot \sqrt{f'_c} \cdot A_j \cdot \Big( 1 + \alpha \cdot \rho_{bl} + \beta \cdot \frac{P}{f'_c \cdot A_j} \Big)
$$

All units must be consistent:  
- \(f'_c\) in MPa  
- \(A_j\) in mm²  
- \(P\) in kN  
- \(V_{proposed}\) in kN
""")

# ===========================
# Display calibrated coefficients
# ===========================
st.subheader("Calibrated Coefficients")
st.markdown("""
- **C** = 11.5508  
- **α (alpha)** = -41.425  
- **β (beta)** = 3531.564
""")

C = 11.5508
alpha = -41.425
beta = 3531.564

# ===========================
# Sidebar inputs
# ===========================
st.sidebar.header("Input Parameters")

fc = st.sidebar.number_input("Concrete compressive strength f'_c (MPa)", min_value=1.0, max_value=100.0, value=30.0, step=1.0)
Aj = st.sidebar.number_input("Web area A_j (mm²)", min_value=1000.0, max_value=1e6, value=100000.0, step=1000.0)
rho_bl = st.sidebar.slider("Longitudinal reinforcement ratio ρ_bl (decimal)", 0.0, 0.1, 0.01, 0.001)
P = st.sidebar.number_input("Axial load P (kN)", min_value=0.0, max_value=5000.0, value=0.0, step=10.0)

# ===========================
# Compute V_proposed
# ===========================
V_proposed = C * np.sqrt(fc) * Aj * (1 + alpha * rho_bl + beta * P / (fc * Aj)) / 1000.0  # kN

st.subheader("Predicted Shear")
st.success(f"V_proposed = {V_proposed:.2f} kN")

# ===========================
# Show detailed calculation
# ===========================
st.markdown(f"""
**Calculation breakdown:**  
V_proposed = {C} × √{fc} × {Aj} × (1 + {alpha}×{rho_bl} + {beta}×{P}/({fc}×{Aj})) / 1000 ≈ **{V_proposed:.2f} kN**
""")

# ===========================
# Dynamic plot
# ===========================
st.subheader("Sensitivity Plot")

st.markdown("See how V_proposed varies with ρ_bl or P while keeping other parameters constant.")

plot_type = st.radio("Choose variable to vary:", ("ρ_bl", "P"))

fig, ax = plt.subplots(figsize=(7,5))

if plot_type == "ρ_bl":
    rho_values = np.linspace(0, 0.1, 100)
    V_values = C * np.sqrt(fc) * Aj * (1 + alpha * rho_values + beta * P / (fc * Aj)) / 1000.0
    ax.plot(rho_values, V_values, color='blue', lw=2)
    ax.set_xlabel("ρ_bl")
else:
    P_values = np.linspace(0, 5000, 100)
    V_values = C * np.sqrt(fc) * Aj * (1 + alpha * rho_bl + beta * P_values / (fc * Aj)) / 1000.0
    ax.plot(P_values, V_values, color='green', lw=2)
    ax.set_xlabel("P (kN)")

ax.set_ylabel("V_proposed (kN)")
ax.set_title("V_proposed Sensitivity")
ax.grid(True)
st.pyplot(fig)

st.markdown("---")
st.markdown("**Developed with Streamlit**")

