import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Setting up the figure with a dark background for space
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')

# Define the planets and their properties
# Data format: (name, orbital radius (AU), orbital period (Earth years), color)
planets = [
    ("Mercury", 0.387, 0.24, "gray"),
    ("Venus", 0.723, 0.62, "orange"),
    ("Earth", 1.0, 1.0, "blue"),
    ("Mars", 1.524, 1.88, "red"),
    ("Jupiter", 5.203, 11.86, "brown"),
    ("Saturn", 9.537, 29.46, "gold"),
    ("Uranus", 19.191, 84.01, "lightblue"),
    ("Neptune", 30.069, 164.79, "blue")
]

# Create orbit circles for reference
max_radius = max(p[1] for p in planets)
for planet in planets:
    orbit = patches.Circle(
        (0, 0), planet[1], fill=False, color='gray', alpha=0.3)
    ax.add_patch(orbit)

# Initialize planet positions with empty data
planet_dots = []
planet_labels = []
for planet in planets:
    # Create a line object for each planet (will be updated as a dot)
    dot = ax.plot([], [], 'o', color=planet[3],
                  markersize=10 if planet[1] < 10 else 15,
                  label=planet[0])[0]
    # Create text label for each planet
    label = ax.text(0, 0, planet[0], color=planet[3], fontsize=8)
    planet_dots.append(dot)
    planet_labels.append(label)

# Add the Sun at the center
sun = plt.Circle((0, 0), 0.5, color='yellow')
ax.add_patch(sun)

# Set the plot limits based on the outermost planet
ax.set_xlim(-max_radius*1.2, max_radius*1.2)
ax.set_ylim(-max_radius*1.2, max_radius*1.2)

# Add title and labels
ax.set_title('Solar System Orbital Motion (Top View)', pad=20)
ax.set_xlabel('Distance (AU)')
ax.set_ylabel('Distance (AU)')


def animate(frame):
    # Calculate positions for each planet
    for i, planet in enumerate(planets):
        # Convert orbital period to angular velocity
        angular_velocity = 2 * np.pi / planet[2]

        # Calculate position as arrays (important fix!)
        x = np.array([planet[1] * np.cos(frame * angular_velocity / 50)])
        y = np.array([planet[1] * np.sin(frame * angular_velocity / 50)])

        # Update planet position
        planet_dots[i].set_data(x, y)

        # Update label position with offset
        offset = 0.5 if planet[1] < 10 else 1
        planet_labels[i].set_position((float(x) + offset, float(y) + offset))

    return planet_dots + planet_labels


# Create animation with appropriate frame rate
anim = FuncAnimation(
    fig,
    animate,
    frames=1000,
    interval=50,  # 50ms between frames = 20 FPS
    blit=True
)

# Add grid for reference
plt.grid(True, alpha=0.2)

# Show the animation
plt.legend(loc='upper right')
plt.show()

# source .venv/bin/activate
# python3 solar_system.py
