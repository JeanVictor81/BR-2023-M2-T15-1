import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DUCKING_HAMMER, RUNNING_HAMMER, JUMPING_HAMMER, HAMMER_TYPE

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
DUCK_TEMP = 8.0

DUCKING_IMGAGE = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMAGE = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMAGE = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

class Dinosaur:
    def __init__ (self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMAGE[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.step_index_duck = 0
        self.jump_vel = JUMP_VEL
        self.duck_temp = DUCK_TEMP
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.power_up_time = 0

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_w] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.jump and not self.duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        elif user_input[pygame.K_s] and not self.dino_duck:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not user_input[pygame.K_s] and not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 9:
            self.step_index = 0

        if self.step_index_duck >= 9:
            self.step_index_duck = 0
    
    def run(self):
        self.image = RUN_IMAGE[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMAGE[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.dino_rect.x = X_POS
            self.jump_vel -= 0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_rect.x = X_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCKING_IMGAGE[self.type][self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 25
        self.step_index_duck += 1
        

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))