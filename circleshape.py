import pygame 


# Base class for game objects 

class CircleShape(pygame.sprite.Sprite): 
    def __init__(self,x,y, radius): 
        # we will be using this later. 
        if hasattr(self, "containers"): 
            super().__init__(self.containers)
        else: 
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius 

    def draw(self): 
        #sub-classess must override
        pass 
    def update (self): 
        #sub-classess must override
        pass

    def collision(self, other): 
        distance  = pygame.math.Vector2.distance_to(self.position, other.position)
        if distance > (self.radius + self.radius): 
            return False 
        return True 


