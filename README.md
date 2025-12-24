<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>Joint Shear Strength-App</h1>

  <p>This project provides an interactive Streamlit application to calculate predicted joint shear, <code>V<sub>proposed</sub></code>, using a calibrated, physics-inspired equation. The app is intended for research purposes and is currently in a <strong>deployment preview stage</strong>, related to an upcoming article on joint shear behavior in reinforced concrete structures.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Interactive Input:</strong> Users can enter concrete strength, web area, reinforcement ratio, and axial load to compute <code>V<sub>proposed</sub></code>.</li>
    <li><strong>Calibrated Coefficients:</strong> The coefficients C, α (alpha), and β (beta) are pre-set based on experimental data.</li>
    <li><strong>Real-time Calculation:</strong> Displays predicted shear instantly along with a detailed calculation breakdown.</li>
    <li><strong>Units Consistency:</strong> Ensures correct units: MPa for <code>f'_c</code>, mm² for <code>A_j</code>, kN for <code>P</code> and <code>V<sub>proposed</sub></code>.</li>
    <li><strong>Web-based:</strong> Accessible directly in a browser at <a href="https://jointshearstrength.streamlit.app/">https://jointshearstrength.streamlit.app/</a> — no installation required.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Open the app using the link: <a href="https://jointshearstrength.streamlit.app/">https://jointshearstrength.streamlit.app/</a></li>
    <li>Adjust the input parameters in the sidebar: <code>f'_c</code>, <code>A_j</code>, <code>ρ_bl</code>, and <code>P</code>.</li>
    <li>The predicted shear <code>V<sub>proposed</sub></code> will be displayed automatically.</li>
    <li>Refer to the calculation breakdown for step-by-step values.</li>
  </ol>

  <h2>Requirements (Optional)</h2>
  <p>If you want to run the app locally instead of via the web link, the following Python packages are required:</p>
  <ul>
    <li>streamlit</li>
    <li>numpy</li>
  </ul>

  <h2>License</h2>
<p>This project is licensed under the <strong>Apache License 2.0</strong>. You may use, modify, and distribute this software under the terms of the license. If you use this software in your work, please provide appropriate credit to the developer.</p>

  <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This app is currently in <strong>deployment preview stage</strong> and related to a research article not yet submitted. Results are preliminary and have not been peer-reviewed.</li>
  </ul>
</body>
</html>
