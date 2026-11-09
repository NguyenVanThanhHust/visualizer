# create and manage window

import pygame


class Window:
    def __init__(self, width=800, height=600, title="3D Visualizer"):
        self.width = width
        self.height = height
        self.title = title

        self.surface = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption(self.title)

    def clear(self, color=(30, 30, 30)):
        self.surface.fill(color)

    def update(self):
        pygame.display.flip()