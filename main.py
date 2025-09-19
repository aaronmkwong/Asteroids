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
    
    # intentional infinite loop
    while True:

        # break when window closes  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # solid blank screen fill

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS) # instantiate player on screen middle

        player.draw(screen) # re-render each frame

        pygame.display.flip() # refresh screen

        dt = clock.tick(60) / 1000 # pause 1/60 second and return delta time in seconds
        
# main() function only called when file directly run
if __name__ == "__main__":
    main()
