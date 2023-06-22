from dino_runner.utils.constants import ICE_TYPE, ICE
from dino_runner.components.power_up.power_up import Power_Up


class Ice(Power_Up):
    def __init__(self):
        self.image = ICE
        self.type = ICE_TYPE
        super().__init__(self.image, self.type)