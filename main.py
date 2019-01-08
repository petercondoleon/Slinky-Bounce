#!/usr/bin/env python3
#
# Slinky Bounce
# An endless jumping game
# https://github.com/petercondoleon/Slinky-Bounce

VERSION = 0.1

from imports import *
from resources import *
from objects import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Slinky Bounce")

    # Load Backgound
    bg, bg_rect = load_image("background.jpg")

    score = 0

    # Initialise objects
    player = Player()

    platform1 = Platform()
    platform2 = Platform()
    platform1.rect = platform1.rect.move(100, 400)
    platform2.rect = platform2.rect.move(300, 200)
    #platform1.rect = platform1.rect.move(random.randint(1,SCREEN_WIDTH), random.randint(1,SCREEN_HEIGHT))
    #platform2.rect = platform2.rect.move(random.randint(1,SCREEN_WIDTH), random.randint(1,SCREEN_HEIGHT))

    # Labels
    scoreLabel = Label('Score: ', 10, 10, 18)
    scoreLabel.draw()

    fpsLabel = Label('FPS: ', SCREEN_WIDTH-45, 5, 10)
    fpsLabel.draw()

    playerSprite = pygame.sprite.RenderPlain(player)
    platformSprites = pygame.sprite.RenderPlain((platform1, platform2))

    # Blit everything to the screen
    screen.blit(bg, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            player.handle_event(event)

        # Draw to screen
        screen.blit(bg, (0, 0))

        playerSprite.update()
        playerSprite.draw(screen)

        platformSprites.update()
        platformSprites.draw(screen)

        # Check collisions only if player is falling
        if player.dy > 0:
            for platform in platformSprites:
                if player.is_collided_with(platform):
                    player.bounce(6.5)
                    score += 5

        scoreLabel.setText(f'Score: {score}')
        scoreLabel.draw()

        fpsLabel.setText(f'FPS: {int(clock.get_fps())}')
        fpsLabel.draw()



        pygame.display.flip()

if __name__ == '__main__': main()
