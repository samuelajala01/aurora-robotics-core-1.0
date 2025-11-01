
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5
L2 = 1.0
L3 = 1.5

def fk(theta1, theta2, theta3):
    """Forward kinematics for a 3R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1)
    y1 = L1*np.sin(theta1)
    x2 = x1 + L2*np.cos(theta1 + theta2)
    y2 = y1 + L2*np.sin(theta1 + theta2)
    x3 = x2 + L3*np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3*np.sin(theta1 + theta2 + theta3)
    return (0, 0), (x1, y1), (x2, y2), (x3,y3)

# --- figure and axes ---
plt.figure(figsize=(10, 10))
ax = plt.subplot(111)
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
ax.set_ylim(- (L1+L2+L3+0.2), L1+L2+L3+0.2)
ax.grid(True, linestyle="--", linewidth=0.5)
ax.set_title("3-Link Planar Arm (use sliders below)")

# initial angles (radians)
theta1_0 = np.deg2rad(30.0)
theta2_0 = np.deg2rad(30.0)
theta3_0 = np.deg2rad(30.0)

# draw initial arm
base, joint, link1, ee = fk(theta1_0, theta2_0, theta3_0)
(link_line,) = ax.plot([base[0], joint[0], link1[0], ee[0]],
                       [base[1], joint[1], link1[1], ee[1]],
                       marker="o", linewidth=3)
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes,
                  va="top", ha="left", fontsize=10,
                  bbox=dict(boxstyle="round", fc="w", ec="0.7"))

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.09, 0.7, 0.03])
slider_ax2 = plt.axes([0.15, 0.05, 0.7, 0.03])
slider_ax3 = plt.axes([0.15, 0.01, 0.7, 0.03])

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0))
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0))
s_theta3 = Slider(slider_ax3, 'θ3 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta3_0))

def update(_):
    th1 = np.deg2rad(s_theta1.val)
    th2 = np.deg2rad(s_theta2.val)
    th3 = np.deg2rad(s_theta3.val)
    b, j, l, e = fk(th1, th2, th3)
    link_line.set_data([b[0], j[0], l[0], e[0]], [b[1], j[1], l[1], e[1]])
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°, θ3={np.rad2deg(th3):.1f}°")
    plt.draw()

s_theta1.on_changed(update)
s_theta2.on_changed(update)
s_theta3.on_changed(update)
update(None)

plt.show()
