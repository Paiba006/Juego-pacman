# player.py
import pygame
from settings import YELLOW, WIDTH, HEIGHT, PLAYER_RADIUS, PLAYER_SPEED

class Player:
    def _init_(self):
        self.radius = PLAYER_RADIUS
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = PLAYER_SPEED
        self.score = 0

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.radius > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.radius < WIDTH:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y - self.radius > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.radius < HEIGHT:
            self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)