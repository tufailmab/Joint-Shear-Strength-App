# Joint Shear Strength-App: Streamlit calculator for V_proposed using calibrated coefficients

import streamlit as st
import numpy as np

# ===========================
# Streamlit page config
# ===========================
st.set_page_config(page_title="Joint Shear Equation Calculator", layout="centered")
st.title("Joint Shear Strength Calculator")

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
# 1. Calibrated coefficients (locked)
# ===========================
C = 11.5508
alpha = -41.425
beta = 3531.564

st.sidebar.header("Calibrated Coefficients (fixed)")
st.sidebar.write(f"C = {C}")
st.sidebar.write(f"alpha = {alpha}")
st.sidebar.write(f"beta = {beta}")

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

# ===========================
# 5. Show calculation breakdown
# ===========================
st.markdown(rf"""
**Calculation breakdown:**  
V_proposed = {C} × √{fc} × {Aj} × (1 + {alpha}×{rho_bl} + {beta}×{P}/({fc}×{Aj})) / 1000 ≈ **{V_proposed:.2f} kN**
""")
