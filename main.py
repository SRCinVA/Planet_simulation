import pygame
import math
pygame.init

WIDTH, HEIGHT = 800, 800  # best to make it square
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # this the pygame "surface," which we can call a "window"
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)

# the Pygame event loop
def main():
    run = True
    clock = pygame.time.Clock()  # this "paces" the speed at which the simulation runs

    while run:
        clock.tick(60) # maximum of 60 times per second
        WIN.fill(WHITE)
        pygame.display.update()

        for event in pygame.event.get():  # basically every possible event in pygame--key presses, mouse movements, etc.
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

main()

