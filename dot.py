# dot.py
import pygame
import random
from settings import WIDTH, HEIGHT, DOT_RADIUS, GREEN

class Dot:
    def _init_(self):
        self.radius = DOT_RADIUS
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(20, HEIGHT - 20)
        self.eaten = False

    def draw(self, screen):
        if not self.eaten:
            pygame.draw.circle(screen, GREEN, (self.x, self.y), self.radius)

    def check_collision(self, player):
        distance = ((self.x - player.x) * 2 + (self.y - player.y) * 2) ** 0.5
        if distance < self.radius + player.radius:
            self.eaten = True
            player.score += 1