import random
import math
import time
from constants import (
    WIDTH, HEIGHT, ENERGY_LOSS_RATE, ENERGY_GAIN, DETECTION_RADIUS,
    MOVEMENT_STEPS, TERRAIN, record_highs, record_lows, DEATH_ANIMATION_DURATION,
    EATING_ANIMATION_DURATION, REPRODUCTION_ANIMATION_DURATION, REPRODUCTION_RATE
)
from utils import draw_star


class Organism:
    def __init__(self, x, y, speed, size, energy_efficiency, escape_ability, recovery_ability):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.speed = speed
        self.base_speed = speed
        self.size = size
        self.energy = 100
        self.energy_efficiency = energy_efficiency
        self.escape_ability = escape_ability
        self.recovery_ability = recovery_ability
        self.health = 100
        self.move_steps = MOVEMENT_STEPS
        self.direction = (random.uniform(-1, 1), random.uniform(-1, 1))
        self.birth_time = time.time()
        self.eating = False
        self.eating_start_time = None
        self.dead = False
        self.death_start_time = None
        self.reproducing = False
        self.reproduction_start_time = None
        self.reproduction_probability = REPRODUCTION_RATE

    def move(self, food_sources):
        if self.dead:
            return

        # Check for nearby food
        nearest_food = None
        nearest_distance = DETECTION_RADIUS
        for food in food_sources:
            distance = math.hypot(self.x - food[0], self.y - food[1])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_food = food

        if nearest_food:
            dx = nearest_food[0] - self.x
            dy = nearest_food[1] - self.y
            distance = math.hypot(dx, dy)
            if distance > 0:
                self.target_x += self.speed * (dx / distance)
                self.target_y += self.speed * (dy / distance)
        else:
            # Move randomly in a consistent direction
            if self.move_steps > 0:
                self.target_x += self.speed * self.direction[0]
                self.target_y += self.speed * self.direction[1]
                self.move_steps -= 1
            else:
                self.direction = (random.uniform(-1, 1), random.uniform(-1, 1))
                self.move_steps = MOVEMENT_STEPS

        self.target_x = max(0, min(WIDTH - 1, self.target_x))
        self.target_y = max(0, min(HEIGHT - 1, self.target_y))
        terrain_type = TERRAIN[int(self.target_y) //
                               10][int(self.target_x) // 10]
        self.energy -= (9 - self.energy_efficiency) * \
            ENERGY_LOSS_RATE * (2 if terrain_type == 'difficult' else 1)
        if terrain_type == 'trap':
            self.health -= (3 - self.escape_ability) * (3 / self.speed) * 0.1

        # Update position gradually for smooth movement
        self.x += (self.target_x - self.x) * 0.1
        self.y += (self.target_y - self.y) * 0.1

    def reproduce(self):
        if random.random() < self.reproduction_probability:
            self.reproducing = True
            self.reproduction_start_time = time.time()
            # Reset probability after reproduction
            self.reproduction_probability = REPRODUCTION_RATE
            child_speed = self.base_speed * random.uniform(0.9, 1.1)
            child_size = self.size * random.uniform(0.9, 1.1)
            child_energy_efficiency = self.energy_efficiency * \
                random.uniform(0.9, 1.1)
            child_escape_ability = self.escape_ability * \
                random.uniform(0.9, 1.1)
            child_recovery_ability = self.recovery_ability * \
                random.uniform(0.9, 1.1)
            return Organism(self.x, self.y, child_speed, child_size, child_energy_efficiency, child_escape_ability, child_recovery_ability)
        return None

    def eat(self):
        self.energy = min(100, self.energy + ENERGY_GAIN)
        self.eating = True
        self.eating_start_time = time.time()
        self.reproduction_probability += 0.01

    def recover(self):
        if self.health < 100:
            self.health = min(100, self.health + self.recovery_ability * 0.1)

    def die(self):
        self.dead = True
        self.death_start_time = time.time()

    def draw(self, screen, font):
        life_time = time.time() - self.birth_time

        if self.dead:
            # Fade out effect
            alpha = 255 * \
                (1 - (time.time() - self.death_start_time) / DEATH_ANIMATION_DURATION)
            if alpha <= 0:
                return  # Skip drawing if fully faded out
            color = (0, int(alpha), 0)
        elif self.eating:
            # Eating effect
            alpha = 255 * \
                (1 - (time.time() - self.eating_start_time) / EATING_ANIMATION_DURATION)
            if alpha <= 0:
                self.eating = False  # End eating animation
                alpha = 255
            color = (255, int(alpha), 0)
        elif self.reproducing:
            # Reproducing effect
            alpha = 255 * \
                (1 - (time.time() - self.reproduction_start_time) /
                 REPRODUCTION_ANIMATION_DURATION)
            if alpha <= 0:
                self.reproducing = False  # End reproducing animation
                alpha = 255
            color = (0, 255, int(alpha))
        else:
            color = (0, 255, 0)

        draw_star(screen, int(self.x), int(self.y), int(self.size), color)

        text = font.render(f"e:{self.energy:.1f} h:{
                           self.health:.1f}", True, (255, 255, 255))
        screen.blit(text, (self.x - text.get_width() //
                    2, self.y - self.size - 15))

        # Update record highs and lows
        record_highs['speed'] = max(record_highs['speed'], self.speed)
        record_highs['size'] = max(record_highs['size'], self.size)
        record_highs['energy_efficiency'] = max(
            record_highs['energy_efficiency'], self.energy_efficiency)
        record_highs['escape_ability'] = max(
            record_highs['escape_ability'], self.escape_ability)
        record_highs['recovery_ability'] = max(
            record_highs['recovery_ability'], self.recovery_ability)
        record_highs['life_time'] = max(record_highs['life_time'], life_time)

        record_lows['speed'] = min(record_lows['speed'], self.speed)
        record_lows['size'] = min(record_lows['size'], self.size)
        record_lows['energy_efficiency'] = min(
            record_lows['energy_efficiency'], self.energy_efficiency)
        record_lows['escape_ability'] = min(
            record_lows['escape_ability'], self.escape_ability)
        record_lows['recovery_ability'] = min(
            record_lows['recovery_ability'], self.recovery_ability)
        record_lows['life_time'] = min(record_lows['life_time'], life_time)
