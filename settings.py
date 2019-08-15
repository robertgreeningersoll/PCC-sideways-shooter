#A class for settings
#Passing one settings object instead of adding settings throughout the code is \
#more efficient.
class Settings():
    """ A class to store all settings for Alien Invasion """
    
    def __init__(self):
        """ initialize the game's settings """
        
        #Screen settings
        self.screen_width = 1200; #screen width
        self.screen_height = 800 #screen height
        self.bg_color = (230, 230, 230)
        
        #Ship Settings
        self.ship_speed_factor = 1.5
        
        #Bullet Settings:
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
