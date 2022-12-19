import random
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager

from dino_runner.components import text_utils
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAME_OVER


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = SCREEN_WIDTH + random.randint(800, 1000)
        self.y_pos_cloud = random.randint(50, 100)

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()

        self.death_count = 0
        self.points = 0
        self.running = True
        
    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            if self.playing == False:
                self.show_menu()
                
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player_heart_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
           
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

        image_2_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image_2_width:
             self.x_pos_cloud = SCREEN_WIDTH + random.randint(2500, 3000)
             self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.x_pos_cloud -= self.game_speed

    def draw_score(self):
        self.points +=1

        if self.points % 100 ==0:
            self.game_speed +=1

        text, text_rect = text_utils.get_score_element(self.points)
        self.player.check_visibility(self.screen)
        self.screen.blit(text, text_rect) 

   ## def save_max_score(self):
    ##    self.list_points = []
     ##   self.points_new = self.points 
      ##  self.list_points.append(self.points_new)

      ##  for self.points_new in self.list_points:
     ##       if self.points
     ##   else:
       ##      self.points < self.points_new       

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        self.print_menu_elements()

        pygame.display.update()
        pygame.display.flip()
        
        self.handle_key_event_on_menu()
       

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message('Press any key to START')
            self.screen.blit(text, text_rect)
        elif self.death_count > 0:
            image, image_rect = text_utils.get_centered_image(GAME_OVER,height = half_screen_height -50 )
            text, text_rect = text_utils.get_centered_message('Press any Key to RESTART ')
            reset, reset_rect = text_utils.get_centered_image(RESET, height= half_screen_height + 70 )
            score, score_text = text_utils.get_centered_message('Your Score is: ' + str(self.points),    height = half_screen_height + 100)
            death, deaht_rect = text_utils.get_centered_message('Death count: ' + str(self.death_count), height = half_screen_height + 150)

            self.screen.blit(score, score_text)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, deaht_rect)
            self.screen.blit(image, image_rect)
            self.screen.blit(reset, reset_rect)

    def handle_key_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                break

            if event.type == pygame.KEYDOWN:
                self.points = 0
                self.run() 
                
