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
    c = 300000000
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


def optical_power_distribution(P_total, rho, lx, ly, lz, FOV, Adet, Ts, G_Con,
                               theta):
    """
    Function to calculate the optical power distribution in a diffuse channel.

    Parameters:
    P_total : float
        Total transmitted power (default is 1 watt).
    rho : float
        Reflection coefficient (default is 0.8).
    lx, ly, lz : float
        Room dimensions in meters.
    FOV : float
        Field of View (in radians).
    Adet : float
        Detector area (default is 1e-4 square meters).
    Ts : float
        Gain of optical filter (default is 1 if no filter is used).
    G_Con : float
        Gain of an optical concentrator (default is 1 if no lens is used).
    theta : float
        Semi-angle at half power (in degrees).

    Returns:
    None (Displays the received power distribution as a 3D plot).
    """

    # Lambertian order of emission
    m = -np.log10(2) / np.log10(np.cos(np.deg2rad(theta)))

    # Number of grid points on each surface
    Nx = int(lx * 3)
    Ny = int(ly * 3)
    Nz = int(round(lz * 3))

    # Calculation grid
    x = np.linspace(-lx / 2, lx / 2, Nx)
    y = np.linspace(-ly / 2, ly / 2, Ny)
    z = np.linspace(-lz / 2, lz / 2, Nz)

    # Create meshgrid for receiver plane (bottom surface)
    XR, YR = np.meshgrid(x, y)  # Only x and y for 2D receiver plane

    # Transmitter position
    TP1 = np.array([0, 0, lz / 2])

    # Initialize reflection from wall 1 (North face)
    h1 = np.zeros((Nx, Ny))

    # Calculation grid area
    dA = lz * ly / (Ny * Nz)
    epsilon = 1e-10  # Small constant to prevent division by zero

    # Loop over each grid point in receiver plane
    for ii in range(Nx):
        for jj in range(Ny):
            RP = np.array([x[ii], y[jj], -lz / 2])  # Receiver position vector

            # Loop over points on the north face (wall 1)
            for kk in range(Ny):
                for ll in range(Nz):
                    WP1 = np.array([-lx / 2, y[kk], z[ll]])  # Point of incidence in wall

                    # Calculate distances and angles
                    D1 = np.linalg.norm(TP1 - WP1) + epsilon  # Distance from transmitter to WP1
                    cos_phi = abs(WP1[2] - TP1[2]) / D1
                    cos_alpha = abs(TP1[0] - WP1[0]) / D1

                    D2 = np.linalg.norm(WP1 - RP) + epsilon  # Distance from WP1 to receiver
                    cos_beta = abs(WP1[0] - RP[0]) / D2
                    cos_psi = abs(WP1[2] - RP[2]) / D2

                    # Check if within field of view (FOV)
                    if abs(np.degrees(np.arccos(cos_psi))) <= np.degrees(FOV):
                        h1[ii, jj] += (Adet * rho * dA * (cos_phi ** m) * cos_alpha * cos_beta * cos_psi) / (
                                    2 * np.pi ** 2 * D1 ** 2 * D2 ** 2)

    # Calculate total received power from all walls (assuming symmetrical reflections for h2, h3, h4)
    h2 = h1  # For simplicity, using h1 to represent all walls
    h3 = h1
    h4 = h1

    # Received power from all walls
    P_rec_A1 = (h1 + h2 + h3 + h4) * P_total * Ts * G_Con

    # Plot the received power distribution
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(XR, YR, P_rec_A1, cmap='viridis')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Received power (W)')
    ax.set_title('Optical Power Distribution in Diffuse Channel')
    plt.show()


def calculate_Drms_3D(C, theta, P_total, Adet, rho, Ts, index, FOV, lx, ly,
                       lz, delta_t):
        # Lambertian order of emission
        m = -np.log10(2) / np.log10(np.cos(np.radians(theta)))

        # Room dimensions and grid
        Nx = int(lx * 3)
        Ny = int(ly * 3)
        Nz = int(round(lz * 3))
        dA = lz * ly / (Ny * Nz)

        x = np.linspace(-lx / 2, lx / 2, Nx + 1)
        y = np.linspace(-ly / 2, ly / 2, Ny + 1)
        z = np.linspace(-lz / 2, lz / 2, Nz + 1)

        # Transmitter and receiver positions
        TP1 = np.array([0, 0, lz / 2])
        TPV = np.array([0, 0, -1])
        RPV = np.array([0, 0, 1])

        # Wall vectors
        WPV1 = np.array([1, 0, 0])
        WPV2 = np.array([0, 1, 0])
        WPV3 = np.array([-1, 0, 0])
        WPV4 = np.array([0, -1, 0])

        G_Con = (index ** 2) / (np.sin(np.radians(FOV)) ** 2)

        Drms = np.zeros((Nx + 1, Ny + 1))
        mean_delay = np.zeros((Nx + 1, Ny + 1))

        for ii in range(Nx + 1):
            for jj in range(Ny + 1):
                RP = np.array([x[ii], y[jj], -lz / 2])
                t_vector = np.arange(0, 25 / delta_t, 1)  # Time vector in ns
                h_vector = np.zeros(len(t_vector))

                # Line of Sight (LOS) channel gain
                D1 = np.linalg.norm(TP1 - RP)
                cosphi = lz / D1
                tau0 = D1 / C
                index_t0 = np.argmin(np.abs(t_vector - round(tau0 / delta_t)))

                if np.abs(np.degrees(np.arccos(cosphi))) <= FOV:
                    h_vector[index_t0] = (m + 1) * Adet * (cosphi ** (m + 1)) / (2 * np.pi * (D1 ** 2))

                # Reflection from walls (loop over 4 walls)
                for wall in [WPV1, WPV2, WPV3, WPV4]:
                    for kk in range(Ny + 1):
                        for ll in range(Nz + 1):
                            WP = np.array([x[kk], y[ll], z[ll]]) * wall
                            D1 = np.linalg.norm(TP1 - WP)
                            cos_phi = abs(WP[2] - TP1[2]) / D1
                            cos_alpha = abs(TP1[0] - WP[0]) / D1

                            D2 = np.linalg.norm(WP - RP)
                            cos_beta = abs(WP[0] - RP[0]) / D2
                            cos_psi = abs(WP[2] - RP[2]) / D2
                            tau = (D1 + D2) / C
                            index_t = np.argmin(np.abs(t_vector - round(tau / delta_t)))

                            if np.abs(np.degrees(np.arccos(cos_psi))) <= FOV:
                                h_vector[index_t] += (m + 1) * Adet * rho * dA * \
                                                     (cos_phi ** m) * cos_alpha * cos_beta * cos_psi / \
                                                     (2 * np.pi ** 2 * D1 ** 2 * D2 ** 2)

                t_vector = t_vector * delta_t
                mean_delay[ii, jj] = np.sum((h_vector ** 2) * t_vector) / np.sum(h_vector ** 2)
                Drms[ii, jj] = np.sqrt(
                    np.sum(((t_vector - mean_delay[ii, jj]) ** 2) * (h_vector ** 2)) / np.sum(h_vector ** 2))

        # Plot the 3D surface
        X, Y = np.meshgrid(x, y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        surf = ax.plot_surface(X, Y, Drms, cmap='viridis')
        fig.colorbar(surf, label="Drms")
        ax.set_xlabel('X [m]')
        ax.set_ylabel('Y [m]')
        ax.set_zlabel('Drms')
        ax.set_title('3D Drms Distribution')
        plt.show()

        return mean_delay, Drms, x, y, z, theta, m, P_total, rho, FOV, TP1
