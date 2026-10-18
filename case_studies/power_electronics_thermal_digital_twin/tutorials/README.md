# Runnable thermal-state baseline

Run the tutorial from the repository root:

<pre><code>python case_studies/power_electronics_thermal_digital_twin/tutorials/thermal_twin_baseline.py</code></pre>

It fits effective thermal resistance $R$ (K/W) and thermal capacitance $C$ (J/K) to a nominal simulated calibration run using

$$
C\frac{dT}{dt}=P-\frac{T-T_a}{R},
$$

then forecasts a run with changed $R$ and ambient temperature. This provides a transparent, physics-based comparison for the ARX forecaster in Module VII. The known shift should produce a nonzero test error; that is the intended transfer diagnostic.

The parameters are exact only because the fixture is generated from the same simple model. They are not measured device properties, and the script does not establish a hardware-calibrated digital twin.
