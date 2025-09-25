from circleshape import * 
from constants import *
import random

# inherit from CircleShape class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    # the asteroid is a circle
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # move straight line constant speed  
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill() # add kill to remove initially

        if self.radius <= ASTEROID_MIN_RADIUS:  
            return # smallest asteroids do nothing
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20,50)

            # first split asteroid 
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = self.velocity.rotate(random_angle) * 1.2

            # second split asteroid 
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = self.velocity.rotate(-random_angle) * 1.2
            

            




