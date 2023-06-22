import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, CLOUD, ICE_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacle.obstacle_manager import ObstacleManager
from dino_runner.components.power_up.power_up_manager import Power_Up_Manager

FONT_STYLE = 'freesansbold.ttf'
GAME_SPEED = 20

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = SCREEN_WIDTH
        self.y_pos_cloud = 150
        self.score = 0
        self.save_score = 0
        self.death_count = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manage = Power_Up_Manager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                
        pygame.display.quit()
        pygame.quit()
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.obstacle_reset()
        self.power_up_manage.reset_power_ups()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manage.update(self)
        self.slow_game_speed()

    def slow_game_speed(self):
        if self.player.type == ICE_TYPE:
            self.game_speed -= 2

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2
    
    def update_death_count(self):
        self.save_score = self.score
        self.score = 0
        self.death_count += 1
        self.game_speed = GAME_SPEED
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) # '#FFFFFF'
        self.draw_background()
        self.draw_cloud()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manage.draw(self.screen)
        self.draw_power_up()
        self.draw_power_up()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_width:
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = SCREEN_WIDTH
        self.x_pos_cloud -= self.game_speed

    def draw_score(self):
        self.show_score = f"Score: {self.game_speed}"
        self.show_text(self.show_score, 50, 1000)

    def draw_power_up(self):
        if self.player.has_power_up:
            time_to_show =round((self.player.power_up_time - pygame.time.get_ticks())/ 1000, 2)
            if time_to_show >= 0:
                self.show_text(f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 50, SCREEN_WIDTH//2)

            else:
                self.player.has_power_up = False
                self.player.type =  DEFAULT_TYPE

    def hundle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        if self.death_count == 0:
            self.screen.fill((255,255,255))
            self.show_text("Press any key to start", SCREEN_HEIGHT/2, SCREEN_WIDTH/2)
        else:
            self.screen.fill((255,255,255))
            self.show_text("Press any key to restart", SCREEN_HEIGHT/2, SCREEN_WIDTH/2)
            self.show_text(f"Your score: {self.save_score}", 200, SCREEN_WIDTH/2)
            self.show_text(f"Your death: {self.death_count}", 220, SCREEN_WIDTH/2)
            
            ## mostrar mensagem de 'Press any key to restart'
            ## mostrar score atingido
            ## mostrar death_count

            ### Resetar score e game_speed quando reiniciar uma nova rodada do jogo
            ### Criar método para remover a repetição de código para o texto

        pygame.display.update()

        self.hundle_events_on_menu()
    
    def show_text(self, text_main, height_pos, width_pos):
        half_screen_height = height_pos
        half_screen_width = width_pos

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(text_main, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height)
        self.screen.blit(text, text_rect)