#Import necessary libraries needed to run and visualize code
import numpy as np # NumPy for numerical computations (sin, cos, radians)
import matplotlib.pyplot as plt # Matplotlib for plotting and visualization
from matplotlib.widgets import Slider # Slider widget for interactive control of joint angles

# --- predefined robot arm link lengths (in arbitrary units) ---
L1 = 1.5 #Defines the length of the first link of the robotic arm
L2 = 1.0 #Defines the length of the second link of the robotic arm

def fk(theta1, theta2):
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    # Computes the coordinates of the first joint (end of link 1)
    x1 = L1*np.cos(theta1) # defines the x-position of joint 1
    y1 = L1*np.sin(theta1) # defines the y-position of joint 1

    # Computes the coordinates of the end-effector (end of link 2)
    x2 = x1 + L2*np.cos(theta1 + theta2) # defines the x-position of end effector
    y2 = y1 + L2*np.sin(theta1 + theta2) # defines the y-position of end effector

    # Return base (0,0), joint 1, and end-effector coordinates as tuples
    return (0, 0), (x1, y1), (x2, y2)

# --- Sets up figure and axes for visualization ---
plt.figure(figsize=(7, 7)) # Creates a new figure window with size 7x7 inches
ax = plt.subplot(111) # Add a single subplot (1 row, 1 column, 1 plot)
ax.set_aspect("equal", adjustable="box")  # Keep equal scaling for x and y axes
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2)  # Set x-axis limits based on arm length
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2)  # Set y-axis limits based on arm length
ax.grid(True, linestyle="--", linewidth=0.5) # Add a dashed grid to the plot
ax.set_title("2-Link Planar Arm (use sliders below)") # Title for the plot window

# Configuring initial joint angles (in radians)
theta1_0 = np.deg2rad(30.0) # Convert 30° to radians for joint 1
theta2_0 = np.deg2rad(30.0)  # Convert 30° to radians for joint 2

# draw initial arm configuration
base, joint, ee = fk(theta1_0, theta2_0)  #Defines coordinates using forward kinematics

# Plot the arm as a line connecting base, joint and end-effector
(link_line,) = ax.plot([base[0], joint[0], ee[0]], # x-coordinates of all points
                       [base[1], joint[1], ee[1]], # y-coordinates of all points
                       marker="o", linewidth=3)     # Add circular markers and set line width for visibility

# Add text on the plot to display end-effector coordinates and joint angles
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes, # Position text relative to axes
                  va="top", ha="left", fontsize=10, # Vertical Alignment:top, Horizontal alignment: left, distinct fontsize for visibility
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) # Text box styling

#Create slider axes (beneath the main plot)
#Slider position: [left, bottom, width, height]
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) # Slider 1 position
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) # Slider 2 position, just below the first

# Define sliders for joint angles θ1 and θ2 (in degrees)
s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #joint angle 1
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))  #joint angle 2

# Define the update function (called when slider values change)
def update(_):
    # Convert slider values (in degrees) to radians
    th1 = np.deg2rad(s_theta1.val)
    th2 = np.deg2rad(s_theta2.val)

     # Compute new joint and end-effector positions
    b, j, e = fk(th1, th2)

    # Update arm line with new coordinates
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]])

     # Update displayed text with current end-effector coordinates and angles
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°")

    # Redraw the plot to reflect new positions
    plt.draw()

# Connect slider movement to the update function
s_theta1.on_changed(update) # Call update() whenever θ1 slider changes
s_theta2.on_changed(update)  # Call update() whenever θ2 slider changes

# Initialize display once at startup
update(None)

# Display the interactive plot window
plt.show()
