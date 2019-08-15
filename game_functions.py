import sys
import pygame as pygame_3
from bullet import Bullet

#the for event loop
#looks for keyboard presses or mouse movements.

#break down the check_events function into 2 parts:
# 1. check keydown events
# 2. check keyup events
# Pass whatever extra parameters are necessary.

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    #print("rveeramani-1111\n");
    if event.key == pygame_3.K_UP:
        #print("rveeramani-2222 right arrow\n");
        ship.moving_up = True;
    elif event.key == pygame_3.K_DOWN:
        #print("rveeramani-3333 left arrow\n");
        ship.moving_down = True;
    elif event.key == pygame_3.K_SPACE:
    	fire_bullet(ai_settings, screen, ship, bullets)
    	
#--------------------------------------------
def fire_bullet(ai_settings, screen, ship, bullets):
	#print("rveeramani-4444 space \n");
	if len(bullets) < ai_settings.bullet_allowed:
		#create a new bullet and add it to the bullets group
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame_3.K_UP:
        ship.moving_up = False;
    elif event.key == pygame_3.K_DOWN:
        ship.moving_down = False;

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame_3.event.get():
        if event.type == pygame_3.QUIT:
            sys.exit()
        elif event.type == pygame_3.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame_3.KEYUP:
            check_keyup_events(event, ship)

# set screen background color.
def update_screen(ai_settings, screen, ship, bullets):
    # Redraw the screen during each pass throuh the loop
    #screen.fill(ai_settings.bg_color);
    screen.fill(ai_settings.bg_color); # set screen background color.
    
    # Draw bullets to screen:
    for bullet in bullets.sprites():
        #print("rveeramani-6666 \n");
        bullet.draw_bullet()
        
    ship.blitme(); # draw the ship by calling blitme() fn.

    
    # Refresh screen. Make the most recently drawn screen visible.
    pygame_3.display.flip()
    
        
def bullets_update(bullets, ai_settings):
    #get rid og bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.right > ai_settings.screen_width:
            bullets.remove(bullet)
    #print(len(bullets))

