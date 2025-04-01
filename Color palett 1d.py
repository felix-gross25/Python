import pygame, sys, random
pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Color palett 1d")
clock = pygame.time.Clock()
RES = WIDTH, HEIGHT = screen.get_size()
FPS = 60
deltatime = 1/FPS 
start_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



def close():
    pygame.quit()
    sys.exit()

def color_palette(start_color, end_color, steps):
    return [(start_color[0] + ((end_color[0] - start_color[0])* step / steps), (start_color[1] + ((end_color[1] - start_color[1])* step / steps)),(start_color[2] + ((end_color[2] - start_color[2])* step / steps))) for step in range(steps)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                close()
            elif event.key == pygame.K_SPACE:
                start_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    colours = color_palette(start_color, end_color, WIDTH)            
    for x in range(len(colours)):
        pygame.draw.line(screen, colours[x], (x, 0), (x, HEIGHT))
    pygame.display.update()
    delta_time = clock.tick(FPS)