import pygame, sys, random, time

pygame.init()
w, h = 480, 800
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

# Colors
RED = (255, 70, 70)
WHITE = (255, 255, 255)
BLACK = (15, 15, 25)
GREEN = (100, 255, 100)

font_title = pygame.font.SysFont("Arial", 40, bold=True)
font = pygame.font.SysFont("Arial", 36)

# Game states
playing = False
game_over = False
score = 0

# Ball setup
radius = 40
x, y = w // 2, h // 2
ball_visible = False
next_ball_time = time.time() + random.uniform(2, 4)

def draw_text_center(text, y_pos, color=WHITE, font_obj=font):
    text_surface = font_obj.render(text, True, color)
    rect = text_surface.get_rect(center=(w // 2, y_pos))
    screen.blit(text_surface, rect)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = e.pos

            if not playing:
                # Start or restart the game
                playing = True
                game_over = False
                score = 0
                ball_visible = False
                next_ball_time = time.time() + random.uniform(2, 4)

            elif ball_visible:
                dist = ((mx - x) ** 2 + (my - y) ** 2) ** 0.5
                if dist <= radius:
                    score += 1
                    ball_visible = False
                    next_ball_time = time.time() + random.uniform(2, 4)

    # Game logic
    screen.fill(BLACK)

    if playing:
        draw_text_center("Focus by Advocate Manish Sharma", 50, WHITE, font_title)
        draw_text_center(f"Score: {score}", 100, GREEN)

        current_time = time.time()

        if not ball_visible and current_time >= next_ball_time:
            x = random.randint(radius + 20, w - radius - 20)
            y = random.randint(200, h - radius - 50)
            ball_visible = True
            ball_appear_time = current_time

        if ball_visible:
            pygame.draw.circle(screen, RED, (x, y), radius)
            if current_time - ball_appear_time > 1.0:
                playing = False
                game_over = True
                ball_visible = False

    elif game_over:
        draw_text_center("Game Over!", h // 2 - 50, RED, font_title)
        draw_text_center(f"Final Score: {score}", h // 2 + 10, WHITE)
        draw_text_center("Tap to Play Again", h // 2 + 70, GREEN)

    else:
        draw_text_center("Focus by Advocate", h // 2 - 60, WHITE)
        draw_text_center("Manish Sharma", h // 2 - 10, WHITE)
        draw_text_center("Tap to Start", h // 2 + 60, GREEN)

    pygame.display.flip()
    clock.tick(60)
