"""
Color Match Game (Pygame)
Fixed layout: stats never overlap, target text centered in swatch.
"""

import pygame, random, time
from collections import deque

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Match Game")

font_big = pygame.font.SysFont(None, 48)
font_small = pygame.font.SysFont(None, 28)

color_list = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 165, 0), (128, 0, 128),
    (0, 255, 255), (255, 192, 203)
]

grid_rows, grid_cols = 4, 4
tile_size = 110   # slightly smaller tiles
tile_margin = 10

target_color = random.choice(color_list)
tiles = []
score = 0
start_time = time.time()
reaction_times = deque(maxlen=10)
attempts = 0
correct_attempts = 0
best_time = float('inf')

def generate_tiles():
    global tiles, target_color
    tiles = []
    for r in range(grid_rows):
        row = []
        for c in range(grid_cols):
            row.append(random.choice(color_list))
        tiles.append(row)
    # ensure at least one tile matches target
    rand_r = random.randint(0, grid_rows-1)
    rand_c = random.randint(0, grid_cols-1)
    tiles[rand_r][rand_c] = target_color

def draw_target_color():
    swatch_width, swatch_height = 400, 100
    swatch_x = (WIDTH - swatch_width) // 2
    swatch_y = 20
    pygame.draw.rect(screen, target_color, (swatch_x, swatch_y, swatch_width, swatch_height))
    text = font_big.render("TARGET COLOR", True, (255, 255, 255))
    text_rect = text.get_rect(center=(swatch_x + swatch_width//2, swatch_y + swatch_height//2))
    screen.blit(text, text_rect)
    return swatch_y + swatch_height + 30  # give more space below

def draw_stats(stats_y):
    avg_time = (sum(reaction_times)/len(reaction_times)) if reaction_times else 0
    accuracy = (correct_attempts/attempts*100 if attempts else 0)
    screen.blit(font_small.render(f"Score: {score}", True, (0, 0, 0)), (20, stats_y))
    screen.blit(font_small.render(f"Best Time: {best_time:.2f}s", True, (0, 0, 0)), (20, stats_y + 25))
    screen.blit(font_small.render(f"Average Time: {avg_time:.2f}s", True, (0, 0, 0)), (20, stats_y + 50))
    screen.blit(font_small.render(f"Accuracy: {accuracy:.0f}%", True, (0, 0, 0)), (20, stats_y + 75))
    return stats_y + 100  # return where grid can start

def draw_tiles(offset_y):
    offset_x = (WIDTH - (grid_cols * tile_size + (grid_cols - 1) * tile_margin)) // 2
    for r in range(grid_rows):
        for c in range(grid_cols):
            rect = pygame.Rect(offset_x + c*(tile_size+tile_margin),
                               offset_y + r*(tile_size+tile_margin),
                               tile_size, tile_size)
            pygame.draw.rect(screen, tiles[r][c], rect)

def reset_game():
    global score, reaction_times, attempts, correct_attempts, best_time
    score = 0
    reaction_times.clear()
    attempts = 0
    correct_attempts = 0
    best_time = float('inf')

generate_tiles()
running = True
while running:
    screen.fill((200, 200, 200))
    stats_y = draw_target_color()
    grid_start_y = draw_stats(stats_y)
    draw_tiles(grid_start_y)  # grid starts after stats

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                reset_game()
                generate_tiles()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            offset_x = (WIDTH - (grid_cols * tile_size + (grid_cols - 1) * tile_margin)) // 2
            for r in range(grid_rows):
                for c in range(grid_cols):
                    rect = pygame.Rect(offset_x + c*(tile_size+tile_margin),
                                       grid_start_y + r*(tile_size+tile_margin),
                                       tile_size, tile_size)
                    if rect.collidepoint(pos):
                        attempts += 1
                        if tiles[r][c] == target_color:
                            elapsed = time.time() - start_time
                            reaction_times.append(elapsed)
                            if elapsed < best_time:
                                best_time = elapsed
                            correct_attempts += 1
                            score += 1
                            target_color = random.choice(color_list)
                            generate_tiles()
                            start_time = time.time()
                        else:
                            score -= 1
                        break
    pygame.display.flip()

pygame.quit()
