import pygame
from src.constants import SCREEN_W, SCREEN_H, FPS
from pygame.locals import QUIT
from src.game import Game

def main():
    
    pygame.init()

    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
    font = pygame.font.SysFont("Arial", 24)

    running = True
    game = Game()
    game_clock = pygame.time.Clock()
    while running:
        delta = game_clock.tick(FPS)
        events = pygame.event.get()

        # process input
        game.handle_input(events)

        # update game world
        game.update(delta)

        # render game world
        game.render(display, font)
        pygame.display.update()

        for e in events:
            if e.type == QUIT:
                running = False


if __name__ == "__main__": # https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()