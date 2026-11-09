# application lifecycle, event handling, and the main loop
import pygame

from .window import Window


class App:
    def __init__(self):
        pygame.init()

        self.window = Window()
        self.clock = pygame.time.Clock()
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def render(self):
        self.window.clear()
        self.window.update()

    def run(self):
        self.running = True

        while self.running:
            self.handle_events()
            self.update()
            self.render()

            self.clock.tick(60)

        self.quit()

    def quit(self):
        pygame.quit()