import sys
import random
import pygame

# sooo..this one kinda works.

# initialising
pygame.init()
clock = pygame.time.Clock()

# setting up the main window
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong!')

sq = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
blue_fixation_point = pygame.Rect(
    screen_width/2 - 15, screen_height/2 - 15, 5, 5)


bg_color = pygame.Color(128, 128, 128)
black = (0, 0, 0)
blue = (0, 0, 255)


allowed_values = list(range(-1, 1+1))
allowed_values.remove(0)


random_value = random.choice(allowed_values)
sq_speed_x = random_value*5
sq_speed_y = random_value*sq_speed_x


# Loop
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Animation
    sq.x += sq_speed_x
    sq.y += sq_speed_y

    # changing speed if clause
    if sq.top <= 0 or sq.bottom >= screen_height:
        sq_speed_y *= -1
    if sq.left <= 0 or sq.right >= screen_width:
        sq_speed_x *= -1

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, black, sq)
    pygame.draw.rect(screen, blue, blue_fixation_point)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
