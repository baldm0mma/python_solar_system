# Solar System Orbital Motion Simulator

This Python project creates an animated visualization of our solar system's planetary orbits from a top-down perspective. The simulation provides an educational tool for understanding the relative orbital periods and distances of the planets in our solar system, with accurate scaling based on astronomical units (AU) and orbital periods.

## Features

The simulation includes several key astronomical features and visual elements:

- Accurate orbital period ratios between planets
- Distance scaling using Astronomical Units (AU)
- Visual size differentiation between inner and outer planets
- Planet-specific color coding for easy identification
- Orbital path indicators
- Planet labels that move with their respective planets
- A centered Sun representation
- Reference grid for distance estimation
- Dark background theme for better visibility

## Prerequisites

To run this simulation, you'll need Python installed on your system along with the following libraries:

```bash
numpy
matplotlib
```

You can install these dependencies using pip:

```bash
pip install numpy matplotlib
```

## Installation and Setup

1. Create a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment:

   - On Unix/MacOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

3. Install the required packages:

   ```bash
   pip install numpy matplotlib
   ```

4. Save the code in a file named `solar_system.py`

5. Run the simulation:
   ```bash
   python solar_system.py
   ```

## How It Works

The simulation operates based on several key components:

### Planet Data Structure

Each planet is represented by a tuple containing four elements:

- Name: The planet's name
- Orbital radius: Distance from the Sun in Astronomical Units (AU)
- Orbital period: Time to complete one orbit in Earth years
- Color: Visual representation color

### Animation Logic

The animation works through these main steps:

1. **Setup Phase:**

   - Creates a dark-themed figure for space visualization
   - Establishes planet orbits as reference circles
   - Places the Sun at the center
   - Initializes planet markers and labels

2. **Animation Phase:**
   - Calculates planet positions using parametric equations:
     - x = r \* cos(ωt)
     - y = r \* sin(ωt)
   - Updates planet positions and labels every frame
   - Maintains relative orbital speeds based on actual orbital periods

### Technical Details

The animation uses matplotlib's FuncAnimation class with the following parameters:

- 1000 total frames
- 50ms interval between frames (20 FPS)
- Blitting enabled for improved performance

Scale and timing details:

- Distances are measured in Astronomical Units (AU)
- One AU equals the average Earth-Sun distance
- Orbital periods are scaled relative to Earth's orbital period
- Animation speed is adjusted for optimal visualization

## Customization

You can modify several aspects of the simulation:

1. **Animation Speed**: Adjust the `interval` parameter in FuncAnimation

   ```python
   interval=50  # Decrease for faster animation, increase for slower
   ```

2. **Planet Size**: Modify the markersize in planet_dots initialization

   ```python
   markersize=10 if planet[1] < 10 else 15  # Adjust these values
   ```

3. **Orbital Path Visibility**: Change the alpha value in orbit creation

   ```python
   alpha=0.3  # Adjust between 0 (invisible) and 1 (solid)
   ```

4. **View Range**: Modify the plot limits multiplier
   ```python
   ax.set_xlim(-max_radius*1.2, max_radius*1.2)  # Adjust 1.2 to zoom in/out
   ```

## Educational Applications

This simulation can be used to demonstrate several astronomical concepts:

1. Relative orbital periods of planets
2. The scale of our solar system using AU
3. The relationship between orbital distance and period
4. Basic concepts of planetary motion

## Known Limitations

- The simulation uses circular orbits rather than elliptical orbits
- Planet sizes are not to scale
- The animation speed is optimized for visualization rather than real-time representation

## Contributing

Feel free to fork this project and enhance it. Some possible improvements:

1. Add elliptical orbits using actual orbital eccentricities
2. Include planetary moons
3. Add more astronomical data display
4. Implement interactive controls for animation speed
5. Add planetary axial tilts and rotations

## License

This project is available under the MIT License. Feel free to use and modify it for educational purposes.

## Acknowledgments

Planet orbital data is based on standard astronomical measurements from NASA's planetary fact sheets.
