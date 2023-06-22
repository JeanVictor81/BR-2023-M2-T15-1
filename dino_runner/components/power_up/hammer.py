from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.power_up.power_up import Power_Up


class Hammer(Power_Up):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)