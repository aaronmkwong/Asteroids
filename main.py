import pygame
from constants import *
from player import *

def main():
    
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # get new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0 # delta time

    # instantiate player on screen middle
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS) 

    # intentional infinite loop
    while True:

        # break when window closes  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # solid blank screen fill
        screen.fill("black") 

        # rotate player
        player.update(dt)

        # re-render each frame
        player.draw(screen) 

        # refresh screen
        pygame.display.flip() 

        # pause 1/60 second and return delta time in seconds
        dt = clock.tick(60) / 1000

# main() function only called when file directly run
if __name__ == "__main__":
    main()
