#module pygame
import pygame as pygame_1
#import settings class
from settings import Settings
#import function
import game_functions as gf
#ship related
from ship import Ship
#bullets related
from bullet import Bullet
from pygame.sprite import Group

def run_game():
    # Initialize and set up screen.
    pygame_1.init();# initializing background settings that pygame needs to work
    ai_settings = Settings();
    screen = pygame_1.display.set_mode((ai_settings.screen_width, \
    ai_settings.screen_height)); # calling pygame.display.set_mode() \
    # to create display window called screen on which we will all the \
    #graphical elements. We provide the window dimensions.
    pygame_1.display.set_caption("Alien Invasion"); # set window caption
    
    #Make as ship
    ship = Ship(ai_settings, screen);
    bullets = Group();
    
    #Start main loop. This is a while loop that contains an event loop. \
    #There is a for loop inside the while loop.  This for loop is the event loop.\
    #The event loop listens for an event. Pressing a key, or moving the mouse is \
    #called an event.
    while True:
        # Start event loop.
        gf.check_events(ai_settings, screen, ship, bullets);# we put the event loop inside this function
        ship.update(); # calling the update function to set movement of ship.
        bullets.update();
        gf.update_screen(ai_settings, screen, ship, bullets);# we put then screen related \
        #functions inside this function.
        
        gf.bullets_update(bullets, ai_settings)

run_game()
