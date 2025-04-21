import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
    
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    astfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
        
        screen.fill(color=(0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        
        updatable.update(dt)
        
        for obj in asteroids:
            if obj.collide(player):
                print(obj, player)
                print('Game over!')
                sys.exit()
        
        dt = clock.tick(60) / 1000
        pygame.display.flip()
    
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

if __name__ == '__main__':
    main()
