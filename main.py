import pygame
import math
pygame.init

WIDTH, HEIGHT = 800, 800  # best to make it square
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # this the pygame "surface," which we can call a "window"
pygame.display.set_caption("Planet Simulation")

WHITE =  (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE =   (100, 149, 237)
RED =    (188, 39, 50)
class Planet:
    AU = 149.6e6 * 1000  # this will simplify the math (in kilometers)
    G = 6.67428e-11      # the constant of gravity
    SCALE = 250/AU # for the pixel-to-meter conversion: one AU will be about 100 pixels
    TIMESTEP = 3600 * 24# what is the elapsing of time we're simulating? We'll make it one day.

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

    def draw(self,win): # this is how we're actually going to get them positioned
        x = self.x * self.SCALE + WIDTH/2  # positioning it from the middle(?)
        y = self.y * self.SCALE + HEIGHT/2 # positioning it from the middle(?)
        pygame.draw.circle(win, self.color, (x,y), self.radius) # this draws the planet on the screen when we call draw()

# the Pygame event loop
def main():
    run = True
    clock = pygame.time.Clock()  # this "paces" the speed at which the simulation runs

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30) # in kgs.   # the sun in the middle, at a size, yellow, etc. ...
    sun.sun = True  # based on our code above, we have to specify that this obejct actually is the sun.

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)  # -1 AU because we're going to the left.
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mercury = Planet
    venus = Planet

    planets = [sun, earth, mars]

    while run:
        clock.tick(60) # maximum of 60 times per second
        # WIN.fill(WHITE)

        for event in pygame.event.get():  # basically every possible event in pygame--key presses, mouse movements, etc.
            if event.type == pygame.QUIT:
                run = False
    
        for planet in planets:  # we go through the list of planets up above
            planet.draw(WIN)  # then we pass the window we want to draw the planet on

        pygame.display.update() # last, we need to update the display

    pygame.quit()

main()

