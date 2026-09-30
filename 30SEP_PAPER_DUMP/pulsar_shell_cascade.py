import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

# ==============================================================================
# Scalar-Angular Torsion (SAT) Framework: Pulsar Equatorial Shell Cascade
# ==============================================================================
# This script models the 3-stage staccato discharge cascade of a rotating 
# 10 km holotype pulsar. It computes the cylindrical velocity profile, maps the
# local worldline inclination theta_4, defines the "lenticular blackout zone"
# where v >= v_crit, and simulates the inward radial propagation of the 
# 14.1° Achromatic Phase Snap.
# ==============================================================================

# Core Physical Constants (SAT Metrological Anchors)
C = 299792458.0              # Speed of light / temporal expansion rate (m/s)
B = 3 / (4 * np.pi)          # Projection Constant ~0.238732
V_CRIT = B * C               # Critical Velocity Threshold ~0.2387c (71,569,348 m/s)
PHI_SNAP = 0.246             # Achromatic Phase Snap (rad) ~14.1°

# Holotype Pulsar Specifications
R_PULSAR = 10000.0           # Radius of the holotype pulsar (10 km in meters)
F_ROT = 1200.0               # Mechanical crust rotation frequency (1200 Hz, slightly super-critical)

def simulate_pulsar_cascade():
    print("================================================================================")
    print("  SIMULATING HOLOTYPE PULSAR EQUATORIAL BREACH & STACCATO CASCADE")
    print("================================================================================\n")
    
    # 1. Calculate critical frequency for first equatorial breach
    # v_equator = R * 2pi * f_rot
    # f_crit occurs when v_equator = v_crit
    f_crit = V_CRIT / (2 * np.pi * R_PULSAR)
    print(f"[ANCHOR] Holotype Pulsar Radius (R): {R_PULSAR/1000:.1f} km")
    print(f"[ANCHOR] Rotation Frequency (f_rot): {F_ROT:.1f} Hz")
    print(f"[CALC]   Critical Breach Frequency (f_crit): {f_crit:.2f} Hz")
    
    if F_ROT < f_crit:
        print(f"[WARN]   f_rot ({F_ROT} Hz) is below critical frequency ({f_crit:.2f} Hz). No breach occurs.")
        return None
    
    print(f"[STATUS] f_rot exceeds f_crit. Equatorial breach confirmed!\n")
    
    # 2. Calculate the boundaries of the Lenticular Blackout Zone (Cylinder-Sphere Intersection)
    # The critical radius from the axis where v = v_crit
    r_crit_axis = V_CRIT / (2 * np.pi * F_ROT)
    print(f"[CALC]   Critical Axis Radius (r_crit): {r_crit_axis:.2f} meters")
    print(f"[GEOM]   A cylinder of radius r_crit = {r_crit_axis/1000:.3f} km is carved through the star.")
    
    # The latitude angle of the boundary on the sphere's surface
    # sin(colatitude) = r_crit / R
    sin_colat = r_crit_axis / R_PULSAR
    colat_boundary = np.arcsin(sin_colat)
    lat_boundary_deg = 90.0 - np.degrees(colat_boundary)
    print(f"[GEOM]   Equatorial 'Staccato Shell' latitude span: ±{lat_boundary_deg:.2f}° around the equator.\n")
    
    # 3. Model the Inward Radial Propagation (Torsion Gradient Wave)
    # Let's set up a 1D radial grid from r_crit to R (the super-critical cylindrical shell)
    num_shells = 50
    radial_grid = np.linspace(r_crit_axis, R_PULSAR, num_shells)
    
    # Calculate pre-glitch worldline inclination theta_4 as a function of r_axis
    # theta_4 = pi/2 - arcsin(v/c)
    v_profile = radial_grid * 2 * np.pi * F_ROT
    theta_4_pre = np.pi/2 - np.arcsin(v_profile / C)
    
    # We simulate the 3-stage cascade:
    # Stage 1: Surface-First Breach at the equator (r_axis = R)
    # Stage 2: Inward Propagation of the 14.1° snap (0.246 rad)
    # Stage 3: Complete Discharge and Phase Recoil
    
    cascade_steps = 5 # Representing 5 snapshots of the inward wave propagation
    cascade_states = []
    
    for step in range(cascade_steps):
        # The fraction of the super-critical shell that has snapped
        snap_fraction = (step + 1) / cascade_steps
        snap_boundary_r = R_PULSAR - snap_fraction * (R_PULSAR - r_crit_axis)
        
        # Apply the Achromatic Phase Snap to the snapped portion
        theta_4_current = np.copy(theta_4_pre)
        snapped_mask = radial_grid >= snap_boundary_r
        theta_4_current[snapped_mask] -= PHI_SNAP
        
        # Compute the local torsion gradient: d(theta_4)/dr
        # Approximated by central difference
        torsion_grad = np.gradient(theta_4_current, radial_grid)
        
        cascade_states.append({
            "step": step + 1,
            "snap_boundary": snap_boundary_r,
            "theta_4": np.degrees(theta_4_current),
            "torsion_grad": torsion_grad
        })
        
        print(f"[CASCADE] Step {step+1}: Snap wave reached r = {snap_boundary_r:.2f} m ({snap_fraction*100:.0f}% of shell discharged).")
        
    return {
        "radial_grid": radial_grid,
        "theta_4_pre": np.degrees(theta_4_pre),
        "r_crit": r_crit_axis,
        "lat_boundary_deg": lat_boundary_deg,
        "cascade_states": cascade_states
    }

def generate_cascade_visualization(sim_data, output_path):
    if sim_data is None:
        return
        
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6.5))
    
    radial_grid = sim_data["radial_grid"]
    theta_pre = sim_data["theta_4_pre"]
    r_crit = sim_data["r_crit"]
    lat_boundary = sim_data["lat_boundary_deg"]
    cascade_states = sim_data["cascade_states"]
    
    # --------------------------------------------------------------------------
    # Panel 1: Cylinder-Sphere Intersection (Lenticular Blackout Zone)
    # --------------------------------------------------------------------------
    ax1.set_aspect('equal')
    
    # Draw the circular cross-section of the pulsar
    pulsar_circle = Circle((0, 0), R_PULSAR, edgecolor='darkblue', facecolor='aliceblue', lw=2, label="Pulsar (10 km)")
    ax1.add_patch(pulsar_circle)
    
    # Draw the rotation axis (vertical)
    ax1.axvline(0, color='gray', linestyle='--', alpha=0.7, label="Rotation Axis")
    
    # Draw the critical velocity cylinder boundaries (vertical lines at x = ±r_crit)
    ax1.axvline(r_crit, color='red', linestyle=':', lw=1.5, label="Critical Boundary (v_crit)")
    ax1.axvline(-r_crit, color='red', linestyle=':')
    
    # Draw the Lenticular Blackout Zone (where cylinder lies inside the sphere)
    # We find the intersection points on the sphere: y = ±sqrt(R^2 - r_crit^2)
    y_intersect = np.sqrt(R_PULSAR**2 - r_crit**2)
    
    # Create polygons representing the lenticular belt on the left and right equators
    angles = np.linspace(-np.arcsin(y_intersect/R_PULSAR), np.arcsin(y_intersect/R_PULSAR), 100)
    
    # Right lenticular belt
    right_x = np.concatenate([[r_crit], R_PULSAR * np.cos(angles), [r_crit]])
    right_y = np.concatenate([[-y_intersect], R_PULSAR * np.sin(angles), [y_intersect]])
    right_poly = Polygon(np.column_stack([right_x, right_y]), facecolor='crimson', alpha=0.4, label="Staccato Shell (Blackout)")
    ax1.add_patch(right_poly)
    
    # Left lenticular belt (mirror)
    left_x = np.concatenate([[-r_crit], -R_PULSAR * np.cos(angles), [-r_crit]])
    left_y = np.concatenate([[-y_intersect], R_PULSAR * np.sin(angles), [y_intersect]])
    left_poly = Polygon(np.column_stack([left_x, left_y]), facecolor='crimson', alpha=0.4)
    ax1.add_patch(left_poly)
    
    ax1.set_xlim(-12000, 12000)
    ax1.set_ylim(-12000, 12000)
    ax1.set_xlabel("Equatorial Plane (meters)", fontsize=10)
    ax1.set_ylabel("Axis Plane (meters)", fontsize=10)
    ax1.set_title("Cylinder-Sphere Intersection\n(Lenticular Blackout)", fontsize=12, fontweight='bold')
    ax1.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    # --------------------------------------------------------------------------
    # Panel 2: Theta_4 Worldline Inclination Profile during Cascade
    # --------------------------------------------------------------------------
    ax2.plot(radial_grid, theta_pre, color='darkblue', linestyle='--', lw=2, label="Pre-Glitch Profile")
    
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(cascade_states)))
    for i, state in enumerate(cascade_states):
        ax2.plot(radial_grid, state["theta_4"], color=colors[i], lw=2, 
                 label=f"Wave Step {state['step']} (r = {state['snap_boundary']/1000:.2f} km)")
        
    ax2.axvline(r_crit, color='red', linestyle=':', lw=1.5)
    ax2.set_xlabel("Radius from Rotation Axis (meters)", fontsize=10)
    ax2.set_ylabel("Worldline Inclination angle (theta_4) [degrees]", fontsize=10)
    ax2.set_title("Inward Cascade of theta_4\n(14.1° Achromatic Phase Snap)", fontsize=12, fontweight='bold')
    ax2.legend(loc='lower center', bbox_to_anchor=(0.5, -0.45), fontsize=9)
    ax2.grid(True, alpha=0.3)
    
    # --------------------------------------------------------------------------
    # Panel 3: Internal Torsion Gradient (d_theta_4 / dr)
    # --------------------------------------------------------------------------
    for i, state in enumerate(cascade_states):
        # Convert gradient to degrees/meter for plotting
        grad_deg_per_m = np.degrees(state["torsion_grad"])
        ax3.plot(radial_grid, grad_deg_per_m, color=colors[i], lw=2, label=f"Step {state['step']}")
        
    ax3.axvline(r_crit, color='red', linestyle=':', lw=1.5)
    ax3.set_xlabel("Radius from Rotation Axis (meters)", fontsize=10)
    ax3.set_ylabel("Torsion Gradient (d_theta_4 / dr) [deg/m]", fontsize=10)
    ax3.set_title("Internal Torsion Gradient Wave\n(Collective Geometric Discharge)", fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    plt.suptitle("SAT Holotype Pulsar Staccato Discharge Cascade Model", fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n[SUCCESS] Generated Cascade Visualization saved to: {output_path}")

if __name__ == "__main__":
    sim_data = simulate_pulsar_cascade()
    generate_cascade_visualization(sim_data, "pulsar_cascade_plot.png")
