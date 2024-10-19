import math
import numpy as np
import matplotlib.pyplot as plt

"""wl = wavelength"""
"""d= distance between transmitter and receiver"""
"""alpha= atmospheric attenuation coefficient"""
"""dt= diameter of transmitter antenna"""
"""dr = diameter of receiver antenna"""
"""pt = power total"""
"""pn = power of ambient noise"""
"""sigma_p = standard deviation of pointing error"""
"""sigma_s= standard deviation due to scintillation"""
"""gamma = initial intensity of optical beam"""
"""cn = refractive structure parameter"""
"""theta= angle of divergence"""
"""theta_mis = mismatch angle divergence"""


def atmospheric_attenuation_loss(gamma, alpha, d):
    return gamma * math.exp(-alpha * d)


def geometric_loss(dr, dt, d, wl, pt):
    return pt * (((dr * wl) / (dt * 4 * math.pi * d))**2)


def pointing_misalignment_loss(d, sigma_p, pt):
    return pt * math.exp(-(d * d) / (2 * sigma_p**2))


def atmospheric_turbulence(pt, cn, d, wl):
    log_amp_var = 1.23 * ((2 * math.pi / wl)**(7 / 6)) * (cn**2) * (d**(11 / 6))
    return pt * math.exp(-log_amp_var / 2)


def polarising_loss_power(pt, theta_mis):
    l_pol = -10*math.log((math.cos(theta_mis))**2, 10)
    return pt*(10**(-l_pol/10))


def ambient_noise(pt, pn):
    return pt + pn


def beam_divergence_loss(theta, d, pt):
    divergence_factor = 1 + ((theta * d)**2)
    return pt / divergence_factor


def scintillation_loss(sigma_s, pt):
    scintillation_factor = math.exp(-(sigma_s**2) / 2)
    return pt * scintillation_factor


def calculate_received_power(p_t, d_r, d):

    p_r = p_t * (d_r / d) ** 2
    return p_r


def calculate_path_loss(p_t, p_r):

    l_p = 10 * np.log10(p_t / p_r)
    return l_p


def calculate_snr(p_r, p_0):

    snr = p_r / p_0
    return snr




k_B = 1.38e-23  # Boltzmann constant (J/K)
E = 1.6e-19  # Electron charge (C)


def calculate_photocurrent(P_received, responsivity):
    """
    Calculate the photocurrent based on received power and responsivity.

    Parameters:
        P_received (array): Received optical power (W).
        responsivity (float): Responsivity of the photodetector (A/W).

    Returns:
        array: Photocurrent (A).
    """
    return responsivity * P_received


def calculate_thermal_noise(T, B, R_load):
    """
    Calculate the thermal noise squared.

    Parameters:
        k_B (float): Boltzmann constant (J/K).
        T (float): Temperature (K).
        B (float): Bandwidth (Hz).
        R_load (float): Load resistance (Ohms).

    Returns:
        float: Thermal noise squared (A^2).
    """
    return (4 * k_B * T * B) / R_load


def calculate_shot_noise(I_photo, B):
    """
    Calculate the shot noise squared.

    Parameters:
        e (float): Electron charge (C).
        I_photo (array): Photocurrent (A).
        B (float): Bandwidth (Hz).

    Returns:
        array: Shot noise squared (A^2).
    """
    return 2 * E * I_photo * B


def calculate_SNR(I_photo, I_shot_squared, I_thermal_squared):
    """
    Calculate the Signal-to-Noise Ratio (SNR).

    Parameters:
        I_photo (array): Photocurrent (A).
        I_shot_squared (array): Shot noise squared (A^2).
        I_thermal_squared (float): Thermal noise squared (A^2).

    Returns:
        array: SNR (unitless).
    """
    return I_photo ** 2 / (I_shot_squared + I_thermal_squared)


def plot_SNR(P_received, SNR):
    """
    Plot the SNR in dB versus received optical power.

    Parameters:
        P_received (array): Received optical power (W).
        SNR (array): Signal-to-Noise Ratio (unitless).
    """
    plt.figure(figsize=(8, 6))
    plt.plot(P_received * 1e3, 10 * np.log10(SNR), label='SNR')
    plt.xlabel('Received Power (mW)')
    plt.ylabel('SNR (dB)')
    plt.title('SNR vs Received Optical Power in FSO')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_fspl(f, d_range, num_points):
    """
    Plot Free Space Path Loss (FSPL) vs Distance.

    Parameters:
    - c: Speed of light (default is 3e8 m/s)
    - f: Frequency (default is 1.9e14 Hz for 1550 nm wavelength)
    - d_range: Tuple defining the minimum and maximum distance (default is (10, 5000) meters)
    - num_points: Number of distance points to generate (default is 100)
    """
    # Distance range (meters)
    d = np.linspace(d_range[0], d_range[1], num_points)

    # Free-space path loss (FSPL)
    FSPL = 20 * np.log10(d) + 20 * np.log10(f) - 20 * np.log10(c) + 20 * np.log10(4 * np.pi)

    # Plot FSPL
    plt.figure(figsize=(8, 6))
    plt.plot(d, FSPL)
    plt.title('Free Space Path Loss (FSPL) vs Distance')
    plt.xlabel('Distance (m)')
    plt.ylabel('FSPL (dB)')
    plt.grid(True)
    plt.show()


def plot_beam_divergence(w_0, lambda_light, d_range, num_points):
    """
    Plot the optical beam divergence vs distance.

    Parameters:
    - w_0: Initial beam waist (default is 0.01 m)
    - lambda_light: Wavelength of the light (default is 1550 nm)
    - d_range: Tuple defining the minimum and maximum distance (default is (10, 5000) meters)
    - num_points: Number of distance points to generate (default is 100)
    """
    # Distance range (meters)
    d = np.linspace(d_range[0], d_range[1], num_points)

    # Beam radius at distance d
    w_d = w_0 * np.sqrt(1 + (lambda_light * d / (np.pi * w_0**2))**2)

    # Plot the beam divergence
    plt.figure(figsize=(8, 6))
    plt.plot(d, w_d)
    plt.title('Optical Beam Divergence')
    plt.xlabel('Distance (m)')
    plt.ylabel('Beam Radius (m)')
    plt.grid(True)
    plt.show()


def los_channel_gain(theta, P_total, Adet, Ts, index, FOV, lx, ly, lz, h,
                     XT, YT):
    """
    Function to calculate the LOS channel gain and received power.

    Parameters:
    theta : float
        Semi-angle at half power (in degrees).
    P_total : float
        Transmitted optical power by individual LED (in watts).
    Adet : float
        Detector physical area of a PD (in square meters).
    Ts : float
        Gain of an optical filter (default is 1 if no filter is used).
    index : float
        Refractive index of a lens at a PD (default is 1.5 if no lens is used).
    FOV : float
        Field of View of a receiver (in radians).
    lx, ly, lz : float
        Room dimensions (in meters).
    h : float
        Distance between the source and the receiver plane (in meters).
    XT, YT : float
        Position of the LED (in meters).

    Returns:
    None (Displays the received power distribution as a 3D plot).
    """

    # Lambertian order of emission
    m = -np.log10(2) / np.log10(np.cos(np.deg2rad(theta)))

    # Gain of an optical concentrator
    G_Con = (index ** 2) / np.sin(FOV)

    # Define receiver plane grid
    Nx = lx * 10
    Ny = ly * 10
    x = np.linspace(-lx / 2, lx / 2, int(Nx))
    y = np.linspace(-ly / 2, ly / 2, int(Ny))
    XR, YR = np.meshgrid(x, y)

    # Distance vector from the source
    D1 = np.sqrt((XR - XT) ** 2 + (YR - YT) ** 2 + h ** 2)

    # Angle vector
    cosphi_A1 = h / D1

    # Channel DC gain for the source
    H_A1 = (m + 1) * Adet * cosphi_A1 ** (m + 1) / (2 * np.pi * D1 ** 2)

    # Received power from source
    P_rec = P_total * H_A1 * Ts * G_Con

    # Convert received power to dBm
    P_rec_dBm = 10 * np.log10(P_rec)

    # Plotting the results
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(XR, YR, P_rec_dBm, cmap='viridis')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Received power (dBm)')
    ax.set_title('Received Power Distribution (dBm)')
    plt.show()

