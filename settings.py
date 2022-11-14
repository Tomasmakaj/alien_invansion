class Settings:
    """A class to store all settings for Alien Invansion."""
    
    def __init__(self):
        """Initizalize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        
        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        
        # Alien Settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 3
        # fleet_direction of 1 represents right and -1 represents left
        self.fleet_direction = 1