import pygame
import sys
import math

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("two dimensional transformation")
BLACK=(0,0,0)
WHITE=(255,255,255)

def translation(x1,y1,x2,y2):
    tx =20
    ty =25
    pygame.draw.line(screen,'red', (x1+tx,y1+ty), (x2+tx,y2+ty))
    
def scaling(x1,y1,x2,y2):
    sx =4
    sy =4
    pygame.draw.line(screen,'blue', (x1*sx,y1*sy), (x2*sx,y2*sy))
    
def rotation(x1,y1,x2,y2):
    theta =90
    th = theta*(math.pi/180)
    x=x2*math.cos(th)-y2*math.sin(th)
    y=x2*math.sin(th)+y2*math.cos(th)
    pygame.draw.line(screen,'yellow', (x1,y1), (x,y))
    
def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        pygame.draw.line(screen,WHITE,(60,60),(100,100))
        translation(60,80,60,100)
        scaling(60,80,60,100)
        rotation(60,60,100,100)
        pygame.display.flip()
        
if __name__=="__main__":
    main()
