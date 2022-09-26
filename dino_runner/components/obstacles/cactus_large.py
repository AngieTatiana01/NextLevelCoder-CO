from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Large_cactus (Obstacle):
    def __init__ (self, image):
        type = random.randint(1,7)
        super().__init__(image,type)
        self.rect.y = 300