# Natural Selection Simulation

This project implements a natural selection simulation using the Pygame library. Organisms move, reproduce, eat, and eventually die in an environment with different types of terrain, simulating the basic principles of evolution and adaptation to the environment. When reproducing, organisms pass their characteristics to their offspring within a variation, allowing evolution over time.

## Project Structure

The project structure is organized as follows:

```
natural-selection-simulation
├── main.py
├── constants.py
├── terrain.py
├── organism.py
├── utils.py
└── assets
    ├── __init__.py
    └── font.py
```

- `main.py`: Entry point of the program. Sets up the Pygame window, manages the main loop, and draws elements on the screen.
- `constants.py`: Contains constants used throughout the project, such as sizes, colors, rates, and simulation parameters.
- `terrain.py`: Responsible for drawing the terrain on the screen.
- `organism.py`: Defines the Organism class, which represents the organisms in the simulation. Includes methods to move, eat, reproduce, and draw the organisms.
- `utils.py`: Contains utility functions, such as creating food and drawing the organisms.
- `assets`: Folder containing additional resources. In this case, it includes font loading.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone this repository:

```sh
git clone https://github.com/your-username/natural-selection-simulation.git
```

2. Navigate to the project directory:

```sh
cd natural-selection-simulation
```

3. Create a virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

4. Install the dependencies:

```sh
pip install pygame
```

## Running

To run the project, use the following command:

```sh
python main.py
```

## Functionality

The simulation starts with an initial population of organisms that move randomly across the screen. They search for food, and upon finding it, consume it to gain energy. Organisms can reproduce and generate offspring with slightly modified characteristics. The simulation tracks and displays the maximum and minimum values of various organism characteristics over time.

## Types of Terrain

The simulation environment consists of three types of terrain:

1. **Normal**:
   - Color: Light Gray `(169, 169, 169)`
   - Effect: Organisms lose energy at a normal rate when moving on this terrain.

2. **Difficult**:
   - Color: Dark Gray `(105, 105, 105)`
   - Effect: Organisms lose energy at double the rate when moving on this terrain due to increased difficulty of movement.

3. **Trap**:
   - Color: Black `(50, 50, 50)`
   - Effect: This terrain is dangerous for organisms. In addition to losing energy, they also lose health proportionally to their escape ability and speed. The lower the organism's escape ability and speed, the greater the damage suffered.

Organisms adapt their behavior based on the type of terrain they encounter:

- **Energy and Health Loss**: Moving through difficult and trap terrains increases the rate of energy loss and can decrease health, affecting the longevity and efficiency of organisms.

## Customization

You can adjust the simulation parameters in the `constants.py` file, such as mutation rate, food appearance intervals, and organism characteristics.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Contact

For questions or suggestions, contact:

- Name: Itallo Nardi
- Email: itallonardi@gmail.com

---

### Acknowledgments

Thank you for using this project!
