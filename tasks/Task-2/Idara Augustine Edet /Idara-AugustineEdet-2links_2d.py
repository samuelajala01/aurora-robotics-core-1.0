
import numpy as np #This is a library used for math.
import matplotlib.pyplot as plt #This is a library used for creating plots
from matplotlib.widgets import Slider #The slider is used to help visualise the change of theta1 and theta2

# --- predefined link lengths (in arbitrary units) ---
L1 = 1.5 #This is the length of the first link. It can be changed to whatever value you desire
L2 = 1.0 #This is the length of the second link. It can also be changed based on your preference

def fk(theta1, theta2): #This is a function used to calculate and return the forward kinematics of the arm
    """Forward kinematics for a 2R planar arm (angles in radians)."""
    x1 = L1*np.cos(theta1) ##This is the formula for x1
    y1 = L1*np.sin(theta1) ##This is the formula for y1
    x2 = x1 + L2*np.cos(theta1 + theta2) #This is the formula for x2
    y2 = y1 + L2*np.sin(theta1 + theta2) #This is the formula for y2
    return (0, 0), (x1, y1), (x2, y2) #This line returns a collection of coordinates, namely the origin, the value of x1,x2,y1 and y2

# --- figure and axes ---
plt.figure(figsize=(7, 7)) #This line defines the size of the plot. It creates a 7 by 7 plot when the code is run
ax = plt.subplot(111) #This is used to create a subplot within a grid of plots
ax.set_aspect("equal", adjustable="box") #Equal makes the scale of the x-axis the same as the scale of the y-axis. Box adjusts the plotting area's shape so that the aspect ratio remains equal
ax.set_xlim(- (L1+L2+0.2), L1+L2+0.2) #This line ensures that the entire arm can be displayed regardless of the length of the links. It specifies the minimum and maximum limit of x
ax.set_ylim(- (L1+L2+0.2), L1+L2+0.2) #This line specifies the maximum and minimum limits of the y-axis
ax.grid(True, linestyle="--", linewidth=0.5) #True enables the gridlines on the plot. Linestyle specifies the type of gridline that will be displayed. Linewidth is used to specify thick the gridlines are on the plot
ax.set_title("2-Link Planar Arm (use sliders below)") #This gives your plot a title

# initial angles (radians)
theta1_0 = np.deg2rad(30.0) #This is the initial angle that theta one has when the plot is displayed after the code is run
theta2_0 = np.deg2rad(30.0) #This is the initial angle theta2 has when the code is run

# draw initial arm
base, joint, ee = fk(theta1_0, theta2_0) #This line assigns the output of the function to three variables; the base, the  joint and the end-effector using the initial angles we assigned in  line 28-29
(link_line,) = ax.plot([base[0], joint[0], ee[0]], #This line is used to plot the arm by indexing the first index of the tuples that hold the coordinates of each part
                       [base[1], joint[1], ee[1]], #This line is used to plot the arm by indexing the second index of the tuples that hold the coordinates of each part
                       marker="o", linewidth=3) # This line adds a marker so we can differentiate between the base, the link and the end-effector, it also sets the width of the plotted line to 3
ee_text = ax.text(0.02, 0.98, "", transform=ax.transAxes, #This line is used to display the information of the plot, i.e. the x and y coordinates of the end-effector and the values of theta1 and theta2
                  va="top", ha="left", fontsize=10, #va means vertical alignment, ha means horizontal alignment. This is used to set where the text lies on the plot. Fontsize sets the fontsize to 10
                  bbox=dict(boxstyle="round", fc="w", ec="0.7")) #boxstyle sets the shape of the box that contains the text. Fc means fill color, ec means edge color

# --- slider axes (beneath plot) ---
slider_ax1 = plt.axes([0.15, 0.05, 0.7, 0.03]) #This line adds a new axis for the slider. The four numbers are in the form of [left, bottom, width, height]. The decimals are actually percentages of the figure
slider_ax2 = plt.axes([0.15, 0.01, 0.7, 0.03]) #This line adds a new axis for the slider. The four numbers are in the form of [left, bottom, width, height]

s_theta1 = Slider(slider_ax1, 'θ1 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta1_0)) #This line defines s_theta1 as a slider, takes the axis for the slider that we defined in the previous lines, gives it a name, takes the minimum and maximum value of the slider and sets the initial position of the slider
s_theta2 = Slider(slider_ax2, 'θ2 (deg)', -180.0, 180.0, valinit=np.rad2deg(theta2_0)) #This line does the same as the previous line for a second slider

def update(_):
    th1 = np.deg2rad(s_theta1.val) #This converts the value of s_theta1 to radians and uses the value to define th1
    th2 = np.deg2rad(s_theta2.val) #This converts the value of s_theta2 to radians and uses the value to define th2
    b, j, e = fk(th1, th2) #This calls the fk function using the values of th1 and th2 as arguments. It assigns the returned tuples to b, j and e
    link_line.set_data([b[0], j[0], e[0]], [b[1], j[1], e[1]]) #This line sets the data of link_line to the new coordinates of b,j and e
    ee_text.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}\nθ1={np.rad2deg(th1):.1f}°, θ2={np.rad2deg(th2):.1f}°") #this line updates the text display
    plt.draw() #This redraws a new plot using the new data everytime this function is called

s_theta1.on_changed(update) #This is used to detect when the user interacts with the slider and automatically calls the update function
s_theta2.on_changed(update) #Does the same for the previous line.
update(None) #This ensures that the arm is visible from the start

plt.show() #This command displays the plot
