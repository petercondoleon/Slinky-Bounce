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
    player.x = SCREEN_WIDTH/2 - player.width/2
    player.y = SCREEN_HEIGHT - player.height*2
    player.dy = -5

    base_platform = Platform()
    base_platform.x = SCREEN_WIDTH/2 - base_platform.width/2
    base_platform.y =SCREEN_HEIGHT - base_platform.height - 5

    platform1 = Platform(100, 400)
    platform2 = Platform(300, 200)

    spikes = Spikes()
    spikes.x = 0
    spikes.y = SCREEN_HEIGHT - spikes.height

    # Labels
    scoreLabel = Label('Score: ', 10, 10, 18)
    scoreLabel.draw()

    fpsLabel = Label('FPS: ', SCREEN_WIDTH-45, 5, 10)
    fpsLabel.draw()

    playerSprite = pygame.sprite.RenderPlain(player)
    platformSprites = pygame.sprite.RenderPlain((base_platform, platform1, platform2))
    spikeSprite = pygame.sprite.RenderPlain(spikes)

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

        spikeSprite.update()
        spikeSprite.draw(screen)

        # Check collisions only if player is falling
        if player.dy > 0:
            for platform in platformSprites:
                if player.is_collided_with(platform):
                    player.bounce(10)

        # Move the platforms down
        if player.y < SCREEN_HEIGHT/2:
            player.y = SCREEN_HEIGHT/2
            score += int(-player.dy)
            for platform in platformSprites:
                platform.dy = -player.dy

        # Reuse low platforms
        for platform in platformSprites:
            if platform.y > SCREEN_HEIGHT:
                platform.y = 0 - platform.height

        scoreLabel.setText(f'Score: {score}')
        scoreLabel.draw()

        fpsLabel.setText(f'FPS: {int(clock.get_fps())}')
        fpsLabel.draw()



        pygame.display.flip()

if __name__ == '__main__': main()
