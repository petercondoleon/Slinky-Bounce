import sys, pygame
pygame.init()

# set up SlinkyB window
size = width, height = 500, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Slinky Bounce")
backgroundIm = pygame.image.load("background.jpg")
dead = False

# Colours
black = (0, 0, 0)

print(pygame.font.get_fonts())
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


# text_display
def text_display(text, size, colour, x, y):
    textFont = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, textFont, colour)
    TextRect = (x, y)
    screen.blit(TextSurf, TextRect)

    # pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(backgroundIm, [0, 0])
        
#    ballrect = ballrect.move(speed)
#    if ballrect.left < 0 or ballrect.right > width:
#        speed[0] = -speed[0]
#    if ballrect.top < 0 or ballrect.bottom > height:
#        speed[1] = -speed[1]
#    screen.blit(ball, ballrect)

    text_display('Score', 18, black, 10, 10)

    white = (255, 255, 255)
    pygame.draw.rect(screen, white, (225, 190, 50, 20))
    pygame.draw.circle(screen, white, (225, 200), 10, 10)
    pygame.draw.circle(screen, white, (275, 200), 10, 10)
    pygame.display.flip()
