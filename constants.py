import random

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
PANEL_WIDTH = 200
FPS = 60
INITIAL_POPULATION = 20
MUTATION_RATE = 0.01
ENERGY_LOSS_RATE = 0.01
ENERGY_GAIN = 100
FOOD_APPEAR_INTERVAL = 1000  # milliseconds
REPRODUCTION_RATE = 0
DETECTION_RADIUS = 100  # distance to detect food
MOVEMENT_STEPS = 20  # number of steps to maintain direction
EATING_ANIMATION_DURATION = 0.5  # seconds
DEATH_ANIMATION_DURATION = 0.5  # seconds
REPRODUCTION_ANIMATION_DURATION = 0.5  # seconds

# Environmental factors
TERRAIN = [[random.choice(['normal', 'difficult', 'trap'])
            for _ in range(WIDTH // 10)] for _ in range(HEIGHT // 10)]

# Colors for terrain types in grayscale
TERRAIN_COLORS = {
    'normal': (169, 169, 169),
    'difficult': (105, 105, 105),
    'trap': (50, 50, 50)
}

# Record highs and lows
record_highs = {
    'speed': 0,
    'size': 0,
    'energy_efficiency': 0,
    'escape_ability': 0,
    'recovery_ability': 0,
    'life_time': 0,
    'max_organisms': 0,
    'max_food': 0
}

record_lows = {
    'speed': float('inf'),
    'size': float('inf'),
    'energy_efficiency': float('inf'),
    'escape_ability': float('inf'),
    'recovery_ability': float('inf'),
    'life_time': float('inf')
}
