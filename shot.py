from circleshape import * 
from constants import *

# shots are small circles
# move at a constant speed in a straight line
# split up asteroids when they collide with them
# spawned by player input (spacebar) move in direction player faces

# inherit from CircleShape class
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    # shot is a small circle
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 0)

    # move straight line constant speed  
    def update(self, dt):
        self.position += self.velocity * dt

