import pygame
from circleshape import CircleShape
import random 
from constants import ASTEROID_MIN_RADIUS 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self): 
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS : 
            return 

        blue_angle = random.uniform(20, 50) 

        pos_asteroid = self.velocity.rotate(blue_angle)
        neg_asteroid = self.velocity.rotate(-blue_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)


        first_asteroid  = pos_asteroid * 1.2 
        second_asteroid = neg_asteroid * 1.2 


