import pygame
import math
pygame.init

WIDTH, HEIGHT = 800, 800  # best to make it square
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # this the pygame "surface," which we can call a "window"
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)

class Planet:
    AU = 149.6e6 * 1000  # this will simplify the math (in kilometers)
    G = 6.67428e-11      # the constant of gravity

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []  # we'll populate this list with coordinates indicating where the planet has orbited
        self.sun = False # we need to be sure that what we're drawing for an orbit is not the sun
        self.distance_to_sun = 0
        # the planets will also need velocities
        self.x_vel = 0
        self.y_vel = 0

# the Pygame event loop
def main():
    run = True
    clock = pygame.time.Clock()  # this "paces" the speed at which the simulation runs

    while run:
        clock.tick(60) # maximum of 60 times per second
        # WIN.fill(WHITE)
        pygame.display.update()

        for event in pygame.event.get():  # basically every possible event in pygame--key presses, mouse movements, etc.
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

main()

