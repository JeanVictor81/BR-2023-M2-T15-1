from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from dino_runner.components.power_up.power_up import Power_Up


class Shield(Power_Up):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)
        