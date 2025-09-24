import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # get GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # delta time

    # create groups to organize objects in static field containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)    
    Shot.containers = (shots, updatable, drawable)

    # instantiate player and asteroids
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS) 
    asteroidfield = AsteroidField()
    
    # intentional infinite loop
    while True:

        # break when window closes  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # solid blank screen fill
        screen.fill("black") 

        # move player via updatable group
        updatable.update(dt)

        # loop over asteroids if collide with ship
        for _ in asteroids:
            if _.collision(player) == True:
                return print("Game over !"), exit()

        # loop over drawables group and render each 
        for _ in drawable:
            _.draw(screen)

        # refresh screen
        pygame.display.flip() 

        # pause 1/60 second and return delta time in seconds
        dt = clock.tick(60) / 1000

# main() function only called when file directly run
if __name__ == "__main__":
    main()
