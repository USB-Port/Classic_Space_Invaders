import pygame

class Invader():

    def __init__(self):
        # --- Class Attributes ---
        #invader position
        self.x = 150
        self.y = 150
        self.speed = [65, 0]

        self.invader = pygame.image.load("invaders.png")
        self.invaderRect = self.invader.get_rect()

        self.soundEffect = pygame.mixer.Sound("fastinvader1.wav")
        
        #these 2 rects represent a partial box around the animation frame I want to retrive
        self.closeAnime = pygame.Rect(20,134,100,65)
        self.openAnime = pygame.Rect(127,134,100,65)

        self.animeBool = True

        # --- Class Methods ---
    def move(self):
        self.invaderRect = self.invaderRect.move(self.speed)

    def flipAnimation(self):
        if self.animeBool :
            self.animeBool = False
        else:
            self.animeBool = True

    def playSoundEffect(self):
        self.soundEffect.play()

    def draw(self, screen):
        if self.animeBool:
            screen.blit(self.invader, self.invaderRect, self.closeAnime)
            
        else:
            screen.blit(self.invader, self.invaderRect, self.openAnime)
            
