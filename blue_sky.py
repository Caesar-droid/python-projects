import sys
import pygame
class BlueSky:
    def run_game(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("New game")
        self.bg_color=(230,255,255)
        while True:
            self.screen.fill(self.bg_color)
            pygame.display.flip()
ai=BlueSky()
ai.run_game()
            