import pygame



pygame.init()
win = pygame.display.set_mode((800, 700))
image = pygame.image.load('map.png')


run = True

btn = [[0, 0, 150, 120, 'a1'], [0, 120, 150, 120, 'b1'], [0, 240, 150, 200, 'c1'], [0, 440, 200, 260, 'd1']]
def a1():
    win.blit(pygame.image.load('a1.png'), (150, 100))


def b1():
    win.blit(pygame.image.load('b1.png'), (150, 100))

def c1():
    win.blit(pygame.image.load('c1.png'), (150, 100))

def d1():
    win.blit(pygame.image.load('d1.png'), (150, 100))

while run:
    win.blit(image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    mpos = pygame.mouse.get_pos()
    for n in btn:
        if mpos[0] > n[0] and mpos[0] < n[0] + n[2] and mpos[1] > n[1] and mpos[1] < n[1] + n[3] and pygame.mouse.get_pressed()[0]:
            eval(n[4]+'()')

    pygame.display.update()

pygame.quit
