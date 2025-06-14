import pygame
import random
import sys
import os
from fruit import Fruit, load_fruit_images

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Cutter")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Game variables
fruit_images = load_fruit_images()
fruits = []
score = 0
spawn_timer = 0
slice_trail = []
game_started = False
selected_mode = None
selected_time = None
game_time_left = 0
high_score = 0
mode_speeds = {'Simple': 2, 'Medium': 4, 'Hard': 6}

# Load high score
def load_high_score(mode):
    path = f"scores_{mode.lower()}.txt"
    if os.path.exists(path):
        with open(path, 'r') as file:
            return int(file.read().strip())
    return 0

def save_high_score(mode, score):
    path = f"scores_{mode.lower()}.txt"
    with open(path, 'w') as file:
        file.write(str(score))

def spawn_fruit():
    fruit_data = random.choice(fruit_images)
    x = random.randint(50, WIDTH - 50)
    y = HEIGHT + 50
    speed = random.randint(mode_speeds[selected_mode], mode_speeds[selected_mode] + 2)
    size_label = random.choice(['small', 'medium', 'large'])
    points = {'small': 15, 'medium': 10, 'large': 5}[size_label]

    fruit = Fruit(
        fruit_data['whole'], x, y, speed, size_label, points,
        fruit_data['half1'], fruit_data['half2'], fruit_data['scale']
    )
    fruits.append(fruit)

def draw_text(text, x, y, color=(255, 255, 255)):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def draw_buttons():
    screen.fill((30, 30, 30))
    draw_text("Select Mode", 320, 50)
    modes = ['Simple', 'Medium', 'Hard']
    for i, mode in enumerate(modes):
        pygame.draw.rect(screen, (100, 200, 100), (150 + i*170, 100, 140, 50))
        draw_text(mode, 175 + i*170, 110)

    draw_text("Select Time", 320, 200)
    times = ['1', '2', '3']
    for i, t in enumerate(times):
        pygame.draw.rect(screen, (200, 100, 100), (150 + i*170, 250, 140, 50))
        draw_text(f"{t} Min", 170 + i*170, 260)
    pygame.display.update()

def handle_button_click(pos):
    global selected_mode, selected_time, game_started, high_score, game_time_left, score
    modes = ['Simple', 'Medium', 'Hard']
    for i, mode in enumerate(modes):
        if pygame.Rect(150 + i*170, 100, 140, 50).collidepoint(pos):
            selected_mode = mode

    times = [1,2,3]
    for i, t in enumerate(times):
        if pygame.Rect(150 + i*170, 250, 140, 50).collidepoint(pos):
            selected_time = t

    if selected_mode and selected_time:
        game_started = True
        score = 0
        high_score = load_high_score(selected_mode)
        game_time_left = selected_time * 60

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    if not game_started:
        draw_buttons()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_button_click(pygame.mouse.get_pos())
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Slicing logic
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pressed:
        slice_trail.append(mouse_pos)
        if len(slice_trail) > 15:
            slice_trail.pop(0)
    else:
        slice_trail.clear()

    # Spawn fruit periodically
    spawn_timer += 1
    if spawn_timer > 40:
        spawn_fruit()
        spawn_timer = 0

    # Move and draw fruits
    for fruit in fruits[:]:
        fruit.move()
        fruit.draw(screen)

        if not fruit.sliced:
            for point in slice_trail:
                if fruit.rect.collidepoint(point):
                    fruit.slice()
                    score += fruit.points
                    break

        if fruit.y + fruit.image.get_height() < -50:
            fruits.remove(fruit)

    # Draw slice trail
    if len(slice_trail) > 1:
        pygame.draw.lines(screen, (255, 0, 0), False, slice_trail, 3)

    # Update and draw score and time
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"High Score: {high_score}", 10, 40)
    draw_text(f"Time Left: {int(game_time_left)}s", 650, 10)
    draw_text(f"Mode: {selected_mode}", 650, 40)

    game_time_left -= 1 / 60
    if game_time_left <= 0:
        game_started = False
        if score > high_score:
            save_high_score(selected_mode, score)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
