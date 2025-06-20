import pygame 
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() 
    dt = 0 

    # creating two objects 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable ,)
    asteroid_field = AsteroidField()
    

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable )

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return

        updatable.update(dt)

        for obj in asteroids: 
            if obj.collision(player): 
                output = sys.exit("Collision Detected")
                print(output)
        for obj in asteroids:
            for shot in shots:
                if obj.collision(shot):
                    shot.kill() 
                    obj.split()


        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/ 1000 

if __name__ == "__main__": 
    main()
