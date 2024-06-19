import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Solar System Model")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the sun and planets
sun = {'color': 'light yellow', 'radius': 20, 'position': (500, 400)}

planets = [
    {'color': 'red', 'radius': 10, 'orbit_radius': 100, 'speed': 1, 'angle': 0}, #mercury
    {'color': 'cyan', 'radius': 12, 'orbit_radius': 150, 'speed': 0.95, 'angle': 0}, #venus
    {'color': 'green', 'radius': 14, 'orbit_radius': 200, 'speed': 0.9, 'angle': 0}, #earth
    {'color': 'orange', 'radius': 13, 'orbit_radius': 250, 'speed': 0.85, 'angle': 0}, #mars
    {'color': 'yellow', 'radius':17, 'orbit_radius': 300, 'speed': 0.8, 'angle': 0}, #jupiter
    {'color': 'dark blue', 'radius': 15, 'orbit_radius': 350, 'speed': 0.75, 'angle': 0}, #satrun
    {'color': 'gray', 'radius': 13, 'orbit_radius': 400, 'speed': 0.7, 'angle': 0}, #uranus
    {'color': 'light blue', 'radius': 14, 'orbit_radius': 450, 'speed': 0.6, 'angle': 0} #neptune
]
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        # Draw the sun
        pygame.draw.circle(screen, sun['color'], sun['position'], sun['radius'])
        # Draw the planets
        for planet in planets:
            x = sun['position'][0] + int(planet['orbit_radius'] * math.cos(math.radians(planet['angle'])))
            y = sun['position'][1] + int(planet['orbit_radius'] * math.sin(math.radians(planet['angle'])))
            pygame.draw.circle(screen, planet['color'], (x, y), planet['radius'])
            planet['angle'] += planet['speed']
            if planet['angle'] >= 360:
                planet['angle'] = 0

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__=="__main__":
    main()
