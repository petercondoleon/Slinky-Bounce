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
    platform3 = Platform()
    platform4 = Platform()

    def reset_game():
        player.is_alive = True
        player.obeys_gravity = True
        player.x = SCREEN_WIDTH/2 - player.width/2
        player.y = SCREEN_HEIGHT - player.height*2
        player.dy = -6 # This gives the player an initial 'jump' when the game starts
        platform1.set_position(300, 100)
        platform2.set_position(100, 300)
        platform3.set_position(186, 500)
        platform4.set_position(80, 600)

    reset_game()

    spikes = Spikes()
    spikes.y = SCREEN_HEIGHT - spikes.height

    # Labels
    scoreLabel = Label('Score: ', 10, 10, 18)
    scoreLabel.draw()

    fpsLabel = Label('FPS: ', SCREEN_WIDTH-45, 5, 10)
    fpsLabel.draw()

    gameOverLabel = Label('GAME OVER', SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2-16, 32)
    gameOverLabel.draw()

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
            if event.type == KEYDOWN:
                if event.key == K_r:
                    if not player.is_alive:
                        reset_game()
                        score = 0
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
                    player.bounce(9)

        # Move the platforms down
        if player.y < SCREEN_HEIGHT/2:
            player.y = SCREEN_HEIGHT/2
            score += int(-player.dy)
            for platform in platformSprites:
                platform.dy = -player.dy

        # Reuse low platforms but randomize
        for platform in platformSprites:
            if platform.y >= SCREEN_HEIGHT+100:
                platform.y = -platform.height
                platform.x = random.randint(25, SCREEN_WIDTH-platform.width-25)

        scoreLabel.setText(f'Score: {score}')
        scoreLabel.draw()

        fpsLabel.setText(f'FPS: {int(clock.get_fps())}')
        fpsLabel.draw()

        if not player.is_alive:
            gameOverLabel.draw()


        pygame.display.flip()

if __name__ == '__main__': main()
