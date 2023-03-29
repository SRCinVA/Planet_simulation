import pygame
import math
pygame.init

WIDTH, HEIGHT = 800, 800  # best to make it square
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # this the pygame "surface," which we can call a "window"
pygame.display.set_caption("Planet Simulation")
