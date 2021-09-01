from pygame import Color, Vector2
from pygame.locals import KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_SPACE
from src.constants import WHITE, BLACK

class Game:

    entities: "list"

    def __init__(self):
        self.entities =[]
    
    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("Move Left")
                if event.key == K_RIGHT:
                    print("Move Right")
                if event.key == K_SPACE:
                    print("Shoot bullet!")
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    print("Stop moving Left")
                if event.key == K_RIGHT:
                    print("Stop moving Right")

    def update(self, delta):
        # Loop through entities
        for i in range(len(self.entities) - 1, -1, -1):
            obj = self.entities[i]
            # Execute entity logic

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        display.fill(BLACK)
        # loop through each entity and render it
        self.render_text(display, font, "Space Invaders", WHITE, (50, 50))