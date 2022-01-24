import numpy as np
import pygame

pygame.init()

# generate window
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1080
COOLDOWN = 1000
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE = [0, 0, 255]
RED = [255, 0, 0]
pygame.display.set_caption("Accuracy Game")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill([255, 255, 255])
pygame.display.flip()


def draw_filled_circle(color):
    # Taille fenetre - le rayon
    x = np.random.randint(SCREEN_WIDTH - 21)
    y = np.random.randint(SCREEN_HEIGHT - 21)
    center = (x, y)
    create_circle = pygame.draw.circle(screen, color, center, 20, 20)
    pygame.display.update()
    return create_circle


def refresh_screen():
    screen.fill([255, 255, 255])
    pygame.display.flip()


def print_score(score):
    fontsize = 25
    font = pygame.font.SysFont('Arial', fontsize)
    score_display = font.render(str(score), True, RED)
    screen.blit(score_display, (1080 - fontsize, 0))


def start_game():
    running = True
    score = 0
    print_score(score)
    circle = draw_filled_circle(BLACK)
    now = pygame.time.get_ticks()
    while running:
        if pygame.time.get_ticks() - now >= COOLDOWN:
            now = pygame.time.get_ticks()
            refresh_screen()
            print_score(score)
            circle = draw_filled_circle(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if circle.collidepoint(event.pos):
                    score += 1
                    now = pygame.time.get_ticks()
                    refresh_screen()
                    print_score(score)
                    circle = draw_filled_circle(BLACK)


def menu():
    intro = True
    fontsize = 25
    font = pygame.font.SysFont('Arial', fontsize)
    play_button = pygame.draw.rect(screen, BLUE, (200, 150, 100, 50))
    screen.blit(font.render('Start', True, (255, 0, 0)), (200, 150))
    quit_button = pygame.draw.rect(screen, BLUE, (400, 150, 100, 50))
    screen.blit(font.render('Quit', True, (255, 0, 0)), (400, 150))
    pygame.display.flip()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.collidepoint(event.pos):
                    intro = False
                    screen.fill(WHITE)
                    pygame.display.flip()
                    start_game()
                if quit_button.collidepoint(event.pos):
                    intro = False
                    pygame.quit()


if __name__ == '__main__':
    menu()
