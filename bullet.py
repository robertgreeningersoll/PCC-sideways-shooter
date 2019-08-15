#Bullet class
import pygame
from pygame.sprite  import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship """
    
    def __init__(self, ai_settings, screen, ship):
        #create bullet object at the ship's current position
        super(Bullet, self).__init__()
        self.screen = screen
        
        #create bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
		ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.top = ship.rect.top
        
        #store the bullet's position as a decimal value.
        self.x = float(self.rect.x)
        
        #set color and speed of bullet
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """ move the bullet up the screen. """
        #update the decimal position of the bullet
        self.x += self.speed_factor
        self.rect.x = self.x
        
    def draw_bullet(self):
        """ draw the bullet to the screen """
        #print("rveeramani-7777 \n")
        pygame.draw.rect(self.screen, self.color, self.rect);
