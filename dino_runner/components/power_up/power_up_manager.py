import random
import pygame

from dino_runner.components.power_up.shield import Shield
from dino_runner.components.power_up.hammer import Hammer
from dino_runner.components.power_up.ice import Ice


class Power_Up_Manager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.number_random = random.random(0, 2)
            self.when_appears += random.randint(200, 300)
            if self.number_random == 0:
                self.power_ups.append(Shield())
            elif self.number_random == 1:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Ice())
            

    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
            
            if self.power_ups == Ice():
                game.game_speed -= 2

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)