import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.randint(0, 2)
            if obstacle_type == 0:
                LargeCactus = Cactus(LARGE_CACTUS)
                LargeCactus.rect.y = 305
                self.obstacles.append(LargeCactus)
            elif obstacle_type == 1:
                SmallCactus = Cactus(SMALL_CACTUS)
                SmallCactus.rect.y = 325
                self.obstacles.append(SmallCactus)
            elif obstacle_type == 2:
                bird = Bird(BIRD)
                bird.rect.y = 245
                self.obstacles.append(bird)
              
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect) and game.player.shield == False:
                game.player_heart_manager.reduce_heart()

                if game.player_heart_manager.heart_count > 0:
                    self.obstacles.pop()
    
                else:   
                   pygame.time.delay(1000)
                   self.obstacles.remove(obstacle)
                   game.playing = False
                   game.player_heart_manager.fill_hearts()
                   game.death_count += 1
                   break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)