import pygame
import random

from dino_runner.components.obstacle.cactus import Cactus
from dino_runner.components.obstacle.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.utils.constants import HAMMER_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        self.random_number = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if self.random_number == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.random_number == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):    
                if not game.player.has_power_up: 
                    pygame.time.delay(500)
                    game.playing = False
                    game.update_death_count()
                    break
                elif game.player.type == HAMMER_TYPE:
                    self.obstacles.remove(obstacle)
                else:
                    pass

    def obstacle_reset(self):
        self.obstacles = []
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)