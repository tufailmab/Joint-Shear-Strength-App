# streamlit_shear_calculator.py
import streamlit as st
import numpy as np

# ===========================
# Streamlit page config
# ===========================
st.set_page_config(page_title="Proposed Shear Equation Calculator", layout="centered")
st.title("Proposed Shear Equation Calculator")

st.markdown(r"""
This app calculates the predicted shear, $V_{\mathrm{proposed}}$, using the proposed equation:

$$
V_{\mathrm{proposed}} = C \cdot \sqrt{f'_c} \cdot A_j \cdot \Big( 1 + \alpha \cdot \rho_{bl} + \beta \cdot \frac{P}{f'_c \cdot A_j} \Big)
$$

**Units:**  
- $f'_c$ in MPa  
- $A_j$ in mm²  
- $P$ in kN  
- $V_{\mathrm{proposed}}$ will be in kN
""")

# ===========================
# 1. Input coefficients
# ===========================
st.sidebar.header("Coefficients")
C = st.sidebar.number_input("C (coefficient)", value=1.0, step=0.01, format="%.3f")
alpha = st.sidebar.number_input("alpha (reinforcement coefficient)", value=0.0, step=0.01, format="%.3f")
beta  = st.sidebar.number_input("beta (axial load coefficient)", value=0.0, step=0.01, format="%.3f")

# ===========================
# 2. Input parameters
# ===========================
st.sidebar.header("Input Parameters")
fc = st.sidebar.number_input("Concrete compressive strength f'_c (MPa)", value=30.0, step=1.0)
Aj = st.sidebar.number_input("Web area A_j (mm²)", value=100000.0, step=1000.0)
rho_bl = st.sidebar.number_input("Longitudinal reinforcement ratio ρ_bl (decimal)", value=0.01, step=0.001)
P = st.sidebar.number_input("Axial load P (kN)", value=0.0, step=1.0)

# ===========================
# 3. Compute V_proposed
# ===========================
V_proposed = C * np.sqrt(fc) * Aj * (1 + alpha * rho_bl + beta * P / (fc * Aj)) / 1000.0  # kN

# ===========================
# 4. Display result
# ===========================
st.subheader("Predicted Shear")
st.write(f"**V_proposed = {V_proposed:.2f} kN**")

# Optional: show formula with values
st.markdown(rf"""
**Using values:**  
C = {C}, alpha = {alpha}, beta = {beta}  
f'_c = {fc} MPa, A_j = {Aj} mm², ρ_bl = {rho_bl}, P = {P} kN  

**Calculation:**  
V_proposed = {C} × √{fc} × {Aj} × (1 + {alpha}×{rho_bl} + {beta}×{P}/({fc}×{Aj})) / 1000 ≈ {V_proposed:.2f} kN
""")
