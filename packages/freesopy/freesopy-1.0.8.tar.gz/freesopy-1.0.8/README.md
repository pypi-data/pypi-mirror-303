<p align="center">
  
</p>

<h1 align="center">Freesopy</h1>

<p align="center">
  <i>A Python package for the implementation of various equations of Free Space Optical Communication</i>
</p>

<hr>


`Freesopy` is designed to simplify the implementation of various mathematical equations used in Free Space Optical Communication. It provides easy-to-use functions that can be integrated into your projects.

## Usaage

You can import `Freesopy` as:

```bash
import freesopy as fso
```
## Some General Equations
P_t: Transmitted power in mW <br>
D_r: Receiver aperture diameter in meters<br>
d: Distance between transmitter and receiver in meters<br>
P_r: Received power in mW<br>
L_p: Path loss in dB<br>
N_0: Noise power spectral density in mW/Hz

<h3>Calculate Received Power</h3>
Power_received = fso.calculate_received_power(P_t, D_r, d)
<h3>Calculate Path Loss</h3>
Path_loss = fso.calculate_path_loss(P_t, P_r)
<h3>Calculate SNR</h3>
SNR = fso.calculate_snr(P_r, N_0)


## Calculation of Losses
wl = wavelength<br>
d= distance between transmitter and receiver<br>
alpha= atmospheric attenuation coefficient<br>
dt= diameter of transmitter antenna<br>
dr = diameter of receiver antenna<br>
pt = power total<br>
pn = power of ambient noise<br>
sigma_p = standard deviation of pointing error<br>
sigma_s= standard deviation due to scintillation<br>
gamma = initial intensity of optical beam<br>cn = refractive structure parameter<br>
theta= angle of divergence<br>
theta_mis = mismatch angle divergence<br>
<br><br>
<h3>Attenuation Loss</h3>

attenuation_loss = fso.atmospheric_attenuation_loss(gamma, alpha, d)

<h3>Geometric Loss</h3>

geo_loss = fso.geometric_loss(dr, dt, d, wl, pt)

<h3>Misalignment Loss</h3>

misalignment_loss = fso.pointing_misalignment_loss(d, sigma_p, pt)

<h3>Atmospheric Turbulence</h3>

turbulence_loss = fso.atmospheric_turbulence(pt, cn, d, wl)

<h3>Polarising Loss Power</h3>

polarising_loss_power = fso.polarising_loss_power(pt, theta_mis)

<h3>Ambient Noise</h3>

ambient_noise = fso.ambient_noise(pt, pn)

<h3>Beam Divergence Loss</h3>

divergence_loss = fso.beam_divergence_loss(theta, d, pt)

<h3>Scintillation Loss</h3>

scintillation_loss = fso.scintillation_loss(sigma_s, pt)

## General Graphs and Calculations
P_received : Received optical power (W) <br>
responsivity : Responsivity of the photodetector (A/W) <br>
T : Temperature (K) <br>
B : Bandwidth (Hz) <br>
R_load : Load resistance (Ohms) <br>
I_photo : Photocurrent (A)<br>
I_shot_squared : Shot noise squared (A^2)<br>
I_thermal_squared : Thermal noise squared (A^2)<br>
SNR : Signal-to-Noise Ratio (unitless) <br>
<br>

<h3>SNR Calculations</h3>


I_photo = fso.calculate_photocurrent(P_received, responsivity)<br><br>
I_thermal_squared = fso.calculate_thermal_noise(T, B, R_load)<br><br>
I_shot_squared = fso.calculate_shot_noise(I_photo, B)<br><br>
SNR = fso.calculate_SNR(I_photo, I_shot_squared, I_thermal_squared)<br><br>
fso.plot_SNR(P_received, SNR)<br><br>

<h3>Free Space Path Loss (FSPL)</h3>
f: Frequency (Hz) <br>
d_range: Tuple defining the minimum and maximum distance in metres<br>
num_points: Number of distance points to generate <br>
<br>
fso.plot_fspl(f, d_range, num_points)

<h3>Divergence of Optical Beam</h3>
w_0: Initial beam waist (m)<br>
lambda_light: Wavelength of the light (nm)<br>
d_range: Tuple defining the minimum and maximum distance (meters)<br>
num_points: Number of distance points to generate<br>
<br>
fso.plot_beam_divergence(w_0, lambda_light, d_range, num_points)

## Channel Modelling
<h3>Simulating the LOS channel gain</h3>
Parameters:<br><br>
    theta : (float)
        Semi-angle at half power (in degrees).<br>
    P_total : (float)
        Transmitted optical power by individual LED (in watts).<br>
    Adet : (float)
        Detector physical area of a PD (in square meters).<br>
    Ts : (float)
        Gain of an optical filter (default is 1 if no filter is used).<br>
    index : (float)
        Refractive index of a lens at a PD (default is 1.5 if no lens is used).<br>
    FOV : (float)
        Field of View of a receiver (in radians).<br>
    lx, ly, lz : (float)
        Room dimensions (in meters).<br>
    h : (float)
        Distance between the source and the receiver plane (in meters).<br>
    XT, YT : (float)
        Position of the LED (in meters).<br>

fso.los_channel_gain(theta, P_total, Adet, Ts, index, FOV, lx, ly, lz, h, XT, YT)

<h3>Plotting the Optical Power Distribution in a Diffuse Channel</h3>

Parameters:<br><br>
    P_total : (float)
        Total transmitted power (default is 1 watt).<br>
    rho : (float)
        Reflection coefficient (default is 0.8).<br>
    lx, ly, lz : (float)
        Room dimensions in meters.<br>
    FOV : (float)
        Field of View (in radians).<br>
    Adet : (float)
        Detector area (default is 1e-4 square meters).<br>
    Ts : (float)
        Gain of optical filter (default is 1 if no filter is used).<br>
    G_Con : (float)
        Gain of an optical concentrator (default is 1 if no lens is used).<br>
    theta : (float)
        Semi-angle at half power (in degrees).<br>

fso.optical_power_distribution(P_total, rho, lx, ly, lz, FOV, Adet, Ts, G_Con, theta)

