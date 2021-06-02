import sys
import random
import pygame

# sooo..this one kinda works!

# initialising
pygame.init()
clock = pygame.time.Clock()

# setting up the main window
screen_width = 672
screen_height = 544
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong!')


def lul():
    return random.randint(-270, 270)


sq = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
sq2 = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
sq3 = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
sq4 = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
ci = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
ci2 = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
ci3 = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
ci4 = pygame.Rect(screen_width/2 + lul(), screen_height/2 + lul(), 30, 30)
uo = pygame.Rect(screen_width/2 + 350, screen_width/2 - 85, 30, 30)
blue_fixation_point = pygame.Rect(
    screen_width/2 - 15, screen_height/2 - 15, 8, 8)


bg_color = pygame.Color(128, 128, 128)
black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
gray = (80, 80, 80)


allowed_values = list(range(-1, 1+1))
allowed_values.remove(0)
allowed_speeds = list(range(1, 2+1))


def setspeeds():
    random_value = random.choice(allowed_values)
    sx = random_value*random.choice(allowed_speeds)
    sy = random_value*sx
    return sx, sy


a, b = setspeeds()
c, d = setspeeds()
e, f = setspeeds()
g, h = setspeeds()
i, j = setspeeds()
k, l = setspeeds()
m, n = setspeeds()
o, p = setspeeds()
q, r = -2, 0

l1startx = screen_width/2 + 350
l1starty = screen_height/2 - 15
l1endx = screen_width/2 + 380
l1endy = screen_height/2 - 15
l2startx = screen_width/2 + 365
l2starty = screen_height / 2 - 30
l2endx = screen_width/2 + 365
l2endy = screen_height/2 + 3


move = False
appear = False

# Loop
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            appear = True
            move = True

    # Animation

    sq.x += a
    sq.y += b
    sq2.x += c
    sq2.y += d
    sq3.x += e
    sq3.y += f
    sq4.x += g
    sq4.y += h

    ci.x += i
    ci.y += j
    ci2.x += k
    ci2.y += l
    ci3.x += m
    ci3.y += n
    ci4.x += o
    ci4.y += p

    if move:
        l1startx += q
        l1endx += q
        l2startx += q
        l2endx += q

    # changing speed if clause
    if sq.top <= 0 or sq.bottom >= screen_height:
        b *= -1
    if sq.left <= 0 or sq.right >= screen_width:
        a *= -1

    if sq2.top <= 0 or sq2.bottom >= screen_height:
        d *= -1
    if sq2.left <= 0 or sq2.right >= screen_width:
        c *= -1

    if sq3.top <= 0 or sq3.bottom >= screen_height:
        f *= -1
    if sq3.left <= 0 or sq3.right >= screen_width:
        e *= -1

    if sq4.top <= 0 or sq4.bottom >= screen_height:
        h *= -1
    if sq4.left <= 0 or sq4.right >= screen_width:
        g *= -1

    if ci.top <= 0 or ci.bottom >= screen_height:
        j *= -1
    if ci.left <= 0 or ci.right >= screen_width:
        i *= -1

    if ci2.top <= 0 or ci2.bottom >= screen_height:
        l *= -1
    if ci2.left <= 0 or ci2.right >= screen_width:
        k *= -1

    if ci3.top <= 0 or ci3.bottom >= screen_height:
        n *= -1
    if ci3.left <= 0 or ci3.right >= screen_width:
        m *= -1

    if ci4.top <= 0 or ci4.bottom >= screen_height:
        p *= -1
    if ci4.left <= 0 or ci4.right >= screen_width:
        o *= -1

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, black, sq)
    pygame.draw.rect(screen, black, sq2)
    pygame.draw.rect(screen, white, sq3)
    pygame.draw.rect(screen, white, sq4)
    pygame.draw.ellipse(screen, black, ci)
    pygame.draw.ellipse(screen, black, ci2)
    pygame.draw.ellipse(screen, white, ci3)
    pygame.draw.ellipse(screen, white, ci4)

    if appear:
        pygame.draw.line(screen, black, (l1startx, l1starty),
                         (l1endx, l1endy), 5)
        pygame.draw.line(screen, black, (l2startx, l2starty),
                         (l2endx, l2endy), 5)

    pygame.draw.rect(screen, blue, blue_fixation_point)

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
