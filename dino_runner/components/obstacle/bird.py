import random

from dino_runner.components.obstacle.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)

        if self.type == 0:
            self.rect.y = 260
        elif self.type == 1:
            self.rect.y = 300