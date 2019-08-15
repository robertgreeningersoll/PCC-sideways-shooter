import pygame as pygame_2

class Ship():
    """ Initialize the ship and set its starting position. """
    
    def __init__(self, ai_settings, screen):
        self.screen = screen;# the screen is where we will draw the ship.
        self.ai_settings = ai_settings;
        
        # load the ship image and get its rect.
        self.image = pygame_2.image.load('./images/ship.bmp'); # this function returns a \
        #surface representing the ship which we store in self.image.
        self.rect = self.image.get_rect(); #accessing self (ship's) rect attribute
        self.screen_rect = screen.get_rect(); #accessing ship's screen's rect attribute
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft
        #self.rect.bottom = self.screen_rect.left
        
        #Store a decimal value for the ship's center
        self.center_y = float(self.rect.centery);
        
        #Movement Flag
        self.moving_up = False;
        self.moving_down = False;
                        
    def blitme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect);#Draw the ship at position specified by \
        #self.rect.
        
    def update(self):
        """ Update the Ship's position based on the movement flag. """
        #Update the ship's center value not the rect.
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor
            
        #Update rect object from self.center
        self.rect.centery = self.center_y
        
        
        
        
        