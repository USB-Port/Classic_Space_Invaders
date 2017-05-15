import sys, pygame
from Invader import *
pygame.init()

size = width, height = 1320, 1240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)



invaderList = []
x = 0
for x in range(5):
    invaderList.append(Invader())
    invaderList[x].invaderRect = invaderList[x].invaderRect.move(115*(x+1),0)

#invader = Invader()   

start_ticks = pygame.time.get_ticks()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    seconds = (pygame.time.get_ticks() - start_ticks)/1000
    if seconds > 1 :
        for invader in invaderList:
            start_ticks = pygame.time.get_ticks()
            invader.playSoundEffect()
            invader.move()
            invader.flipAnimation()

            if invader.invaderRect.left < 0 or invader.invaderRect.right > width :
                invader.speed[0] = -invader.speed[0]
                invader.invaderRect = invader.invaderRect.move(0, 120)


    screen.fill(black)
    for invader in invaderList:
        invader.draw(screen)
  
    pygame.display.flip()