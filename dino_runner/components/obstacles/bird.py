from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Bird (Obstacle):
    BIRD_HEIGHTS = [10000,1000,10000 , 40, 250, 30, 250, 250]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)    
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.rect.x = 1000
        self.index = 0

    def draw(self, SCREEN):
        
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1
