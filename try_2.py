import pygame
import sys

pygame.init()
pygame.display.set_caption('bresenham line algorithm')
screen=pygame.display.set_mode((500,300))

def bresenham_line(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    slope=dy/dx
    x,y=x1,y1
    screen.set_at((x,y),'white')
    if slope<=1:
        p=2*dy-dx
        while x!=x2:
            x+=1
            if p<0:
                p+=2*dy
            else:
                y+=1 if y1<y2 else -1
                p+=2*(dy-dx)
            screen.set_at((x,y),'white')
    else:
        p=2*dy-dx
        while y!=y2:
            y+=1 if y1<y2 else -1
            if p<0:
                p+=2*dx
            else:
                x+=1
                p+=2*(dy-dx)
                screen.set_at((x,y),'white')

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        bresenham_line(20,50,100,100)
        pygame.display.flip()

if __name__=="__main__":
    main()

