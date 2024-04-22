import numpy as np
import matplotlib.pyplot as plt

def calculate_primary_rainbow(angle_of_incidence, refractive_index, droplet_radius):
    # Convert angle to radians
    angle_of_incidence_rad = np.radians(angle_of_incidence)
    
    # Calculate critical angle
    critical_angle = np.arcsin(1 / refractive_index)
    
    # Check if critical angle is exceeded
    if angle_of_incidence_rad > critical_angle:
        return None  # Total internal reflection occurs, no rainbow
    
    # Calculate deviation angle for primary rainbow
    deviation_angle = 2 * np.arcsin((1 - np.sin(angle_of_incidence_rad)) / refractive_index)
    
    # Calculate angular positions of rainbow colors
    rainbow_angles = np.degrees(np.arcsin(np.linspace(0, 1, 100) * np.sin(deviation_angle)))
    
    return rainbow_angles

def calculate_secondary_rainbow(angle_of_incidence, refractive_index, droplet_radius):
    # Convert angle to radians
    angle_of_incidence_rad = np.radians(angle_of_incidence)
    
    # Calculate critical angle
    critical_angle = np.arcsin(1 / refractive_index)
    
    # Check if critical angle is exceeded
    if angle_of_incidence_rad > critical_angle:
        return None  # Total internal reflection occurs, no rainbow
    
    # Calculate deviation angle for primary rainbow
    deviation_angle_primary = 2 * np.arcsin((1 - np.sin(angle_of_incidence_rad)) / refractive_index)
    
    # Calculate deviation angle for secondary rainbow
    deviation_angle_secondary = np.pi - deviation_angle_primary
    
    # Calculate angular positions of rainbow colors for secondary rainbow
    rainbow_angles_secondary = np.degrees(np.arcsin(np.linspace(0, 1, 100) * np.sin(deviation_angle_secondary)))
    
    return rainbow_angles_secondary

def calculate_intensity_vs_angle(angle_of_incidence, refractive_index, droplet_radius):
    # Convert angle to radians
    angle_of_incidence_rad = np.radians(angle_of_incidence)
    
    # Calculate critical angle
    critical_angle = np.arcsin(1 / refractive_index)
    
    # Check if critical angle is exceeded
    if angle_of_incidence_rad > critical_angle:
        return None, None, None  # Total internal reflection occurs, no rainbow
    
    # Calculate deviation angle for primary rainbow
    deviation_angle_primary = 2 * np.arcsin((1 - np.sin(angle_of_incidence_rad)) / refractive_index)
    
    # Calculate deviation angle for secondary rainbow
    deviation_angle_secondary = np.pi - deviation_angle_primary
    
    # Calculate scattering angles for intensity calculation
    scattering_angles = np.linspace(0, np.pi, 100)
    
    # Calculate intensity using Airy theory
    intensity_primary = (1 + np.cos(scattering_angles - deviation_angle_primary))**2
    intensity_secondary = (1 + np.cos(scattering_angles - deviation_angle_secondary))**2
    
    return np.degrees(scattering_angles), intensity_primary, intensity_secondary

# Parameters
refractive_index_water = 1.333  # Refractive index of water
droplet_radius = 1.0  # Radius of water droplet in micrometers

# Incident angle range (in degrees)
incident_angles = np.linspace(0, 90, 91)

# Calculate rainbow angles for each incident angle
rainbow_data = []
secondary_rainbow_data = []
for angle in incident_angles:
    rainbow_angles = calculate_primary_rainbow(angle, refractive_index_water, droplet_radius)
    if rainbow_angles is not None:
        rainbow_data.append(rainbow_angles)
        
    rainbow_angles_secondary = calculate_secondary_rainbow(angle, refractive_index_water, droplet_radius)
    if rainbow_angles_secondary is not None:
        secondary_rainbow_data.append(rainbow_angles_secondary)

# Plotting primary and secondary rainbows
plt.figure(figsize=(10, 6))
for angles in rainbow_data:
    plt.plot(angles, np.linspace(0, 1, len(angles)), color='blue', label='Primary Rainbow')
for angles_secondary in secondary_rainbow_data:
    plt.plot(angles_secondary, np.linspace(0, 1, len(angles_secondary)), color='red', linestyle='--', label='Secondary Rainbow')
plt.xlabel('Angle (degrees)')
plt.ylabel('Normalized Intensity')
plt.title('Primary and Secondary Rainbows')
plt.xlim(0, 180)
plt.ylim(0, 1)
plt.legend()
plt.grid(True)
plt.show()

# Calculate intensity vs. scattering angle for a specific incident angle
angle_of_incidence_example = 40  # Example incident angle in degrees
scattering_angles, intensity_primary_example, intensity_secondary_example = calculate_intensity_vs_angle(angle_of_incidence_example, refractive_index_water, droplet_radius)

# Plotting intensity vs. scattering angle
plt.figure(figsize=(10, 6))
plt.plot(scattering_angles, intensity_primary_example, color='blue', label='Primary Rainbow')
plt.plot(scattering_angles, intensity_secondary_example, color='red', linestyle='--', label='Secondary Rainbow')
plt.xlabel('Scattering Angle (degrees)')
plt.ylabel('Intensity')
plt.title("Intensity vs. Scattering Angle")
plt.legend()
plt.grid(True)
plt.show()
