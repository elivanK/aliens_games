import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    # A class to represnet a single alien in the fleet 
    
    def __init__(self, ai_settings, screen):
        # Initialize the alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien image and set its rect attribute 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left corner of the screen
        # Add space to the left of it that's equal to the alien's width
        self.rect.x = self.rect.width
        # And a space above it equal to its height
        self.rect.y = self.rect.height
        
        # Store the alien's exact position
        self.x = float(self.rect.x)
    
    def blitme(self):
        # Draw the alien at its current location
        self.screen.blit(self.image, self.rect)
    
    # Each time we update the aline position
    # We move it to the right by the amount stored in alien_speed_factor    
    def update(self):
        # Move the alien right
        # With self.x we track the alien's exact position
        # and with that value to update position of alien's rect
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x