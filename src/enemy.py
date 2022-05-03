import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        """Updates the screen, creates surface object image, get the rectangle for positioning, sets other attributes
        arg = pygame.sprite"""
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
      """ Changes both the x and y coordinates of the internal rectangle object by a random value: -1, 0, or 1.
"""
      self.rect.x += random.choice(range(-1, 2))
      self.rect.y += random.choice(range(-1, 2))