import pygame, sys, random
import numpy as np
pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Color palett 2d")

clock = pygame.time.Clock()
RES = WIDTH, HEIGHT = screen.get_size()
FPS = 60
deltatime = 1/FPS 

color00, color10, color01, color11 = [None] * 4

def generate_base_colours():
    global color00, color10, color01, color11
    color00 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color01 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color10 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color11 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

color00, color10, color01, color11 = (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)



palett_width = HEIGHT
palett_height = HEIGHT

def close():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                close()
            elif event.key == pygame.K_SPACE:
                generate_base_colours()
    palett = np.array([np.linspace(np.linspace(color00, color01, palett_width, True, False, np.uint8, 0)[r], np.linspace(color10, color11, palett_width, True, False, np.uint8, 0)[r], palett_height, True, False, np.uint8, 0) for r in range(palett_width)], dtype= np.uint8)
    screen.blit(pygame.surfarray.make_surface(palett), (0, 0))
    pygame.display.update()
    delta_time = clock.tick(FPS)