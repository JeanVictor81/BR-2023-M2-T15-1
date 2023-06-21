import random

from dino_runner.components.obstacle.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        self.step_index = 0
        super().__init__(image, self.type)

        if self.type == 0:
            self.rect.y = 260
        elif self.type == 1:
            self.rect.y = 300
    
    def draw(self, screen):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        if self.step_index >= 10:
            self.step_index = 0
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.step_index += 1