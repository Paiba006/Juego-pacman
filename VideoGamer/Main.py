# main.py
import pygame
from settings import WIDTH, HEIGHT, BLACK, WHITE
from player import Player
from dot import Dot

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Básico")

player = Player()
dots = [Dot() for _ in range(20)]

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw(screen)

    for dot in dots:
        dot.check_collision(player)
        dot.draw(screen)

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Puntos: {player.score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()