import random
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        if len(self.obstacles) == 0:
            cactus_size = random.randint(0, 1)
            if cactus_size == 0:
                LargeCactus = Cactus(LARGE_CACTUS)
                LargeCactus.rect.y = 305
                self.obstacles.append(LargeCactus)
            else:
                SmallCactus = Cactus(SMALL_CACTUS)
                SmallCactus.rect.y = 325
                self.obstacles.append(SmallCactus)

        for Obstacle in self.obstacles:
            Obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(Obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)