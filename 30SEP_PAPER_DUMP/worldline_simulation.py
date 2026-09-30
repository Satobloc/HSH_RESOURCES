import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ==============================================================================
# Scalar-Angular Torsion (SAT) Framework: 9-Phase Worldline Cycle Simulation
# ==============================================================================
# This script simulates the kinematics of a 4D superhelical worldline (filament)
# undergoing rotational stress. It computes the local worldline inclination
# theta_4, models the 14.1° Achromatic Phase Snap at the Critical Velocity 
# Threshold (v_crit ≈ 0.2387c), and performs 4D coordinate transformations 
# using the SO(4) rotation group.
# ==============================================================================

# Core SAT Constants
C = 299792458.0              # Speed of light / temporal expansion rate (m/s)
B = 3 / (4 * np.pi)          # Projection Constant ~0.23873
V_CRIT = B * C               # Critical Velocity Threshold ~0.2387c (71,569 km/s)
PHI_SNAP = 0.246             # Achromatic Phase Snap (rad) ~14.1°
ELL_F = 0.7937e-15           # Fundamental Filament Scale (meters)
EPSILON = 2.0e-21            # Minimal Curvature Regulator (meters)

def calculate_theta_4(v, snapped=False):
    """
    Computes the local worldline inclination theta_4 as a function of velocity.
    By default, theta_4 is the angle between the worldline tangent and the 
    time normal expansion vector.
    """
    v_ratio = np.clip(v / C, -1.0, 1.0)
    theta_raw = np.pi/2 - np.arcsin(v_ratio) # Angle from temporalnormal (90° - arcsin(v/c))
    if snapped:
        theta_raw -= PHI_SNAP
    return theta_raw

def get_so4_rotation_matrix(angle_xy, angle_zw):
    """
    Generates a 4D SO(4) rotation matrix.
    SO(4) is isomorphic to SU(2) x SU(2) / Z_2, which is decomposed here into 
    independent planar rotations (XY spatial and ZW spatio-temporal).
    """
    c_xy, s_xy = np.cos(angle_xy), np.sin(angle_xy)
    c_zw, s_zw = np.cos(angle_zw), np.sin(angle_zw)
    
    R = np.array([
        [c_xy, -s_xy, 0, 0],
        [s_xy,  c_xy, 0, 0],
        [0,  0, c_zw, -s_zw],
        [0,  0, s_zw,  c_zw]
    ])
    return R

def simulate_9_phases():
    """
    Simulates the 9 distinct phases of the worldline rotation cycle.
    """
    phases_data = []
    
    # 9-Phase Definition Table
    phase_definitions = [
        (1, "Perpendicular Baseline", 0.0, False),
        (2, "Sub-Critical Forward Lean", 0.12 * C, False),
        (3, "Critical Boundary (Pre-Snap)", V_CRIT, False),
        (4, "Achromatic Phase Snap (Post-Snap)", V_CRIT, True),
        (5, "Tangent Configuration", C, False),
        (6, "Over-Rotation (Slicing)", 1.2 * C, False),
        (7, "Inverted Original (Negative Lean)", -0.15 * C, False),
        (8, "Reverse Tangent", -C, False),
        (9, "Return to Perpendicular", 0.0, False)
    ]
    
    # Initial 4D trajectory tangent vector (massless baseline, orthogonal to space)
    X_0 = np.array([0.0, 0.0, 0.0, 1.0])
    
    print(f"{'Phase':<6} | {'Regime/Phase Name':<35} | {'Velocity/c':<12} | {'theta_4 (deg)':<14} | {'Status/Action':<15}")
    print("-" * 92)
    
    for idx, name, v, snap in phase_definitions:
        theta = calculate_theta_4(v, snapped=snap)
        theta_deg = np.degrees(theta)
        
        # Calculate the 4D coordinate shift under the rotation connection
        # Using theta as the tilt in the spatio-temporal plane (XW plane)
        R_st = np.array([
            [np.sin(theta), 0, 0, -np.cos(theta)],
            [0,             1, 0,  0],
            [0,             0, 1,  0],
            [np.cos(theta), 0, 0,  np.sin(theta)]
        ])
        X_prime = R_st.dot(X_0)
        
        v_c = v / C
        action = "RESET SNAP" if snap else "Continuous"
        print(f"{idx:<6} | {name:<35} | {v_c:<12.4f} | {theta_deg:<14.2f} | {action:<15}")
        
        phases_data.append({
            "phase": idx,
            "name": name,
            "velocity": v,
            "v_ratio": v_c,
            "theta_4_rad": theta,
            "theta_4_deg": theta_deg,
            "vector": X_prime,
            "snap": snap
        })
        
    return phases_data

def generate_visualization(data, output_path):
    """
    Generates a publication-quality visualization of the 9-Phase Worldline Cycle.
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    # Extract values for plotting
    thetas_deg = [p["theta_4_deg"] for p in data]
    thetas_rad = [p["theta_4_rad"] for p in data]
    v_ratios = [p["v_ratio"] for p in data]
    names = [p["name"] for p in data]
    phases = [p["phase"] for p in data]
    
    # Plot the trajectory phases
    colors = plt.cm.plasma(np.linspace(0, 1, 9))
    
    for i in range(len(data)):
        # Represent the worldline tangent as a vector pointing at the inclination angle
        r = abs(v_ratios[i]) if abs(v_ratios[i]) > 0 else 0.1
        ax.annotate(f"P{phases[i]}", xy=(thetas_rad[i], r), xytext=(thetas_rad[i], r + 0.15),
                    arrowprops=dict(arrowstyle="->", color=colors[i], lw=2),
                    color=colors[i], fontweight='bold', fontsize=10)
        
        # Draw the line segment representing the worldline tilt
        ax.plot([0, thetas_rad[i]], [0, r], color=colors[i], lw=3, label=f"Phase {phases[i]}: {names[i]}")
        
    # Draw Critical Velocity Threshold boundary (v = B ≈ 0.2387)
    circle_angles = np.linspace(0, 2*np.pi, 200)
    ax.plot(circle_angles, [B]*200, color='red', linestyle='--', lw=1.5, label=f'Critical Boundary v_crit (B ≈ 0.2387c)')
    
    ax.set_title("SAT 9-Phase Worldline Rotation & Holonomy Cycle", fontsize=16, fontweight='bold', pad=30)
    ax.set_rmax(1.3)
    ax.set_rticks([0.2387, 0.5, 1.0])
    ax.set_yticklabels(['v_crit', '0.5c', 'c'], fontsize=10, fontweight='bold')
    ax.grid(True)
    
    plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1.0), fontsize=9)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n[SUCCESS] Visualized worldline cycle saved to: {output_path}")

if __name__ == "__main__":
    print("================================================================================")
    print("      SIMULATING COHERENT 4D WORLDLINE ROTATIONAL HARMONICS & SNAPS")
    print("================================================================================\n")
    data = simulate_9_phases()
    generate_visualization(data, "worldline_phases.png")
