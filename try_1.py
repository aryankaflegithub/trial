import pygame
import sys

pygame.init()
pygame.display.set_caption('dda line algorithm')
screen=pygame.display.set_mode((500,300))

def draw_line(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    step=max(abs(dx),abs(dy))
    x_inc=dx/step
    y_inc=dy/step
    x=x1
    y=y1
    for i in range(step):
        screen.set_at((round(x),round(y)),'white')
        x+=x_inc
        y+=y_inc


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        draw_line(20,20,100,100)
        pygame.display.flip()


if __name__=='__main__':
    main()