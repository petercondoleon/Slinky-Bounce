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
    player.dy = -6 # This gives the player an initial 'jump' when the game starts

    platform1 = Platform(300, 175)
    platform2 = Platform(100, 375)
    platform3 = Platform(212, 575) # The first platform for the player
    platform4 = Platform(80, 775)

    spikes = Spikes()
    spikes.y = SCREEN_HEIGHT - spikes.height

    # Labels
    scoreLabel = Label('Score: ', 10, 10, 18)
    scoreLabel.draw()

    fpsLabel = Label('FPS: ', SCREEN_WIDTH-45, 5, 10)
    fpsLabel.draw()

    # Need to add the objects into sprite groups for the game
    playerSprites = pygame.sprite.RenderPlain(player)
    platformSprites = pygame.sprite.RenderPlain((platform1, platform2, platform3, platform4))
    spikeSprites = pygame.sprite.RenderPlain(spikes)

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

        playerSprites.update()
        playerSprites.draw(screen)

        platformSprites.update()
        platformSprites.draw(screen)

        spikeSprites.update()
        spikeSprites.draw(screen)

        # Check collisions only if player is falling
        if player.dy > 0:
            for platform in platformSprites:
                if player.bottom_collides_with(platform):
                    player.bounce(9.5)

        # Move the platforms down
        if player.y < SCREEN_HEIGHT/2:
            player.y = SCREEN_HEIGHT/2
            score += int(-player.dy)
            for platform in platformSprites:
                platform.dy = -player.dy

        # Reuse low platforms but randomize
        for platform in platformSprites:
            if platform.y >= 800:
                platform.y = -platform.height
                platform.x = random.randint(25, SCREEN_WIDTH-platform.width-25)

        scoreLabel.setText(f'Score: {score}')
        scoreLabel.draw()

        fpsLabel.setText(f'FPS: {int(clock.get_fps())}')
        fpsLabel.draw()



        pygame.display.flip()

if __name__ == '__main__': main()
