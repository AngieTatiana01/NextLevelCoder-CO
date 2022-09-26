from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus_large import Large_cactus
import pygame

class Obstaclemanager: 
    def __init__(self):
        self.obstacles = []

    def update (self, game):
        if len(self.obstacles) == 0:
            new_obstacle = Cactus(SMALL_CACTUS)
            new_obstacle_large = Cactus(LARGE_CACTUS)
            new_obstacle_bird = Bird(BIRD)

            self.obstacles.append(new_obstacle)
            self.obstacles.append(new_obstacle_bird)
            self.obstacles.append(new_obstacle_large)
            

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield: 
                    self.obstacles.remove(obstacle)
                else:
                    pygame.time.delay(500)
                    game.playing = False 
                    break;  
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    
    
        

    
                        