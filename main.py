import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    # delta time - amount of time since the last frame was drawn
    dt = 0

    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # update player class, so all instances will have group assigned
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # spawn player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)
    
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        # update objects position
        for object in updatable:
            object.update(dt)

        # check for collision
        for asteroid in asteroids:
            if asteroid.is_collided(player):
                print("Game Over!")
                sys.exit()
            # check bullet collisions with asteroids
            for shot in shots:
                if asteroid.is_collided(shot):
                    shot.kill()
                    asteroid.split()
                    break       
        
        # re-render objects
        for object in drawable:
            object.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
