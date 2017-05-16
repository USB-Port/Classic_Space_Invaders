import sys, pygame
from Invader import *
from Player import *

#initialize pygame
pygame.init()

#set the size = width = 1320 and the hight to 1240
size = width, height = 1320, 1240

#define the the color black to use as a fill for BG
black = 0, 0, 0

#Set the display
screen = pygame.display.set_mode(size)

#Set the amount a key is repeated when held down
pygame.key.set_repeat(5,10)

#Create a list to hold many invaders, this is done to reduce code and use the power of OO code
invaderList = []

#instatiate the player object
player = Player()

# Simular to int i = 0
x = 0
#For loop from 0 to 7
for x in range(8):
    #instatiate a invader object then append it to the invader list
    invaderList.append(Invader())
    #Change the starting location of each new invader to the right by 120px
    invaderList[x].invaderRect = invaderList[x].invaderRect.move(120*(x+1),0)

#Get the starting ticks for a basic timer. Noob timer
start_ticks = pygame.time.get_ticks()

#The game loop, exits when ESC key is pressed
while 1:
    #loop through all events in the queue
    for event in pygame.event.get():
        #if the event is a key pressed down
        if event.type == pygame.KEYDOWN:
            #if that key that was press was A and the player is still within the playable area
            if event.key == pygame.K_a and player.playerRect.left > 0 :
                #move the player left
                player.movePlayerLeft()
            #If that key that was pressed down was d and the player is still within the screen area, I.E not off screen hiding
            if event.key == pygame.K_d and player.playerRect.right < width :
                #move the player right
                player.movePlayerRight()
            #If the escape key is pressed down
            if event.key == pygame.K_ESCAPE:
                #quit the game 
                sys.exit()
    #number of seconds is calculated with the power of maths. This is in millisecond. Divide by 1000 to get seconds. lower number means faster invader
    seconds = (pygame.time.get_ticks() - start_ticks) / 200

    #if seconds is greater then 1 then it time to move the invaders one time
    if seconds > 1 :
        #for each invader in the list of invaders, we do this code
        for invader in invaderList:
            #reset the starting clicks
            start_ticks = pygame.time.get_ticks()
            #Play the sound effects.
            invader.playSoundEffect()
            #move the invader
            invader.move()
            #flip the animation. The animation has 2 frames so flip a bool ez pz lol. 
            invader.flipAnimation()

            #if the invader will travle off the screen, reverse its direction the other way
            if invader.invaderRect.left < 0 or invader.invaderRect.right > width :
                #flip the speed vector 
                invader.speed[0] = -invader.speed[0]
                #move the invader 120px down
                invader.invaderRect = invader.invaderRect.move(0, 120)

    #Cover the whole screen with black pixels, this is done to erase the old sprites
    screen.fill(black)
    #loop through all the invader in the list of invaders
    for invader in invaderList:
        #draw the invaders
        invader.draw(screen)

    #draw the player
    player.drawPlayer(screen)

    #Flip the buffer. Pygame draws all images to back buffer so you need to flip it to see what was drawn. 
    #Double buffer is built into pygame and used for smooth animation
    pygame.display.flip()