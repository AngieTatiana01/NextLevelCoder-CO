
import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_COLOR
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import Obstaclemanager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('dino_runner/sonido/cancion.mp3')
        pygame.mixer.music.play(-1)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = 0
        self.y_pos_cloud = 50
        self.player = Dinosaur()
        self.obstacle_manager = Obstaclemanager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.font = pygame.font.Font('freesansbold.ttf', 24)
    

    def run(self):
        self.power_up_manager.reset_power_ups(self.points)
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.score()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.show_score()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.player.check_invincibility(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed +=1
       

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (image + self.x_pos_cloud, self.y_pos_cloud))
        if self.x_pos_cloud <= -image:
            self.screen.blit(CLOUD, (image + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = 1000
        self.x_pos_cloud -= self.game_speed


    def menu (self):

        text = self.font.render("Press any Key to Start", True, (0, 0, 0))
        self.screen.blit(text, (100, 100))


    def show_score(self):
        score = self.font.render("Score :" + str(self.points), True, (0, 0, 0))
        self.screen.blit(score, (10, 10))

    