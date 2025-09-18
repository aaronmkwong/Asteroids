import pygame
from  constants import *

def main():
    
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # get new GIU window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    # intentional infinite loop
    while True:

        # break when window closes  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # solid blank screen fill
        
        pygame.display.flip() # refresh screen

        dt = clock.tick(60) / 1000 # pause 1/60 second and return delta time in seconds

# main() function only called when file directly run
if __name__ == "__main__":
    main()
