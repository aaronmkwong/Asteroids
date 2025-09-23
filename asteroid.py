from circleshape import * 

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

