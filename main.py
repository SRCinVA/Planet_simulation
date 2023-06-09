import pygame
import math
pygame.init()

WIDTH, HEIGHT = 800, 800  # best to make it square
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # this the pygame "surface," which we can call a "window"
pygame.display.set_caption("Planet Simulation")

WHITE =  (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE =   (100, 149, 237)
RED =    (188, 39, 50)
DARK_GRAY = (80, 78, 81)

FONT = pygame.font.SysFont("arial", 16)

class Planet:
    AU = 149.6e6 * 1000  # this will simplify the math (in kilometers)
    G = 6.67428e-11      # the constant of gravity
    SCALE = 250/AU # for the pixel-to-meter conversion: one AU will be about 100 pixels
    TIMESTEP = 3600 * 24 # what is the elapsing of time we're simulating? We'll make it one day.

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
        
        if len(self.orbit) > 2: # we'll do this only if we have 3 or more points in the list
            updated_points = [] # this is where we place the points the planets have been located.
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2 # says he's getting to scale to draw them properly. Dividing by 2 to get them from the middle of the screen.
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x,y))

            pygame.draw.lines(win, self.color, False, updated_points, 2) # pass in the window, the color, unenclosed status, the list of points, and the thickness of the line.
        
        pygame.draw.circle(win, self.color, (x,y), self.radius) # this draws the planet on the screen when we call draw()

        if not self.sun:
            # pygame.font.init()
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)} km", 1, WHITE) # this FONT object creates a text object taht you can draw, rounded to 1 decimal point. The second "1" means anti-aliasing.
            # to draw it on the screen
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2)) # this is to adjust where the text object shows up.

    def attraction(self, other): # this is the force attraction between two objects
        other_x, other_y = other.x, other.y
        # to figure out distance between objects:
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance # if the other object is the sun, then we just go ahead and store it for later use
        
        force = self.G * self.mass * other.mass / distance ** 2  # this is the straight-line force of attraction between the objects    
        theta = math.atan2(distance_y, distance_x)  # calculates the angle
        force_x = math.cos(theta) * force # for the x position force
        force_y = math.sin(theta) * force # for the y position force
        return force_x, force_y

    def update_position(self, planets): # remember that each planet effects each other
        total_fx = total_fy = 0  # this is the total of forces exerted on the planet that is not itself
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy 

        self.x_vel += total_fx / self.mass * self.TIMESTEP # it's additive because the velocity is changing over time. As x increse, y decreases, and vice versa.
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        # from acceleration, you get velocity, and from velocity, you get displacement (i.e., distance):
        self.x += self.x_vel * self.TIMESTEP  # this updates the x position using the velocity
        self.y += self.y_vel * self.TIMESTEP  # this updates the y position using the velocity
        self.orbit.append((self.x, self.y))  # this gets appended to orbit[] 

# the Pygame event loop
def main():
    run = True
    clock = pygame.time.Clock()  # this "paces" the speed at which the simulation runs

    # each planet has one negative and one positive velocity; this way, they move in the same direction.
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30) # in kgs.   # the sun in the middle, at a size, yellow, etc. ...
    sun.sun = True  # based on our code above, we have to specify that this obejct actually is the sun.

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)  # -1 AU because we're going to the left. Planet.AU is a variable insie the Planet class.
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0 , 8, DARK_GRAY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60) # maximum of 60 times per second
        WIN.fill((0, 0, 0)) # this redraws the black background (60 times per second?); otherwise, we keep seeing the old planets from past orbits

        for event in pygame.event.get():  # basically every possible event in pygame--key presses, mouse movements, etc.
            if event.type == pygame.QUIT:
                run = False
    
        for planet in planets:  # we go through the list of planets up above
            planet.update_position(planets)
            planet.draw(WIN)  # then we pass the window we want to draw the planet on

        pygame.display.update() # last, we need to update the display

    pygame.quit()

main()

