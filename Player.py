import pygame

class Player() :
    def __init__(self):
        self.speed = [5,0]
        self.player = pygame.image.load("invaders.png")
        self.playerRect = self.player.get_rect()
        self.playerRectClip = pygame.Rect(26,337,194,90)
        self.playerRect = self.playerRect.move(10, 1150)


    def movePlayerLeft(self):
        self.playerRect = self.playerRect.move(-self.speed[0], 0)

    def movePlayerRight(self):
        self.playerRect = self.playerRect.move(self.speed)

    def drawPlayer(self, screen):
        screen.blit(self.player, self.playerRect, self.playerRectClip)
    

