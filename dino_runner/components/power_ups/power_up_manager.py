import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import HAMMER_LIFE, HAMMER_TYPE, SHIELD_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.points = 0
        self.hammer_life = HAMMER_LIFE
    
    def update(self, point, game_speed, player):
        self.generate_power_ups(point)
        for powerup in self.power_ups:
            powerup.update(game_speed, self.power_ups)

            if (player.dino_rect.colliderect(powerup.rect)):
                if powerup.type == SHIELD_TYPE:
                   powerup.start_time = pygame.time.get_ticks()
                   player.shield = True
                   player.hammer = False
                   player.type = powerup.type
                   powerup.start_time = pygame.time.get_ticks()
                   player.shield_time_up = powerup.start_time + ((random.randint(5,8) * 1000))
                   self.power_ups.remove(powerup)

                elif powerup.type == HAMMER_TYPE:
                    powerup.start_time = pygame.time.get_ticks()
                    player.shield = False
                    player.hammer = True
                    player.type = powerup.type
                    powerup.start_time = pygame.time.get_ticks()
                    player.hammer_time_up = powerup.start_time + ((random.randint(5,8) * 1000))
                    self.power_ups.remove(powerup)
  



    def draw(self, screen):
        for powerup in self.power_ups:
            powerup.draw(screen)
    
    def generate_power_ups(self, points):
        if len(self.power_ups) == 0:
            if self.when_appers == points:
                self.when_appers = random.randint(self.when_appers + 120, 500 + self.when_appers)
                self.power_ups.append(Hammer())
                self.power_ups.append(Shield())

            
