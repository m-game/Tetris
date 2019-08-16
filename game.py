import sys

import pygame
from pygame.locals import *


class Game(object):
    def __init__(self, size, caption):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()

    def update(self):
        self.screen.fill(BLACK)

    def event(self, event):
        pass

    def run_forever(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                self.event(event)
            self.update()
            pygame.display.update()
            self.clock.tick(60)


# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Tetris(Game):
    BLOCK_SIZE = 30
    ITEM = {
        'I': [(0, 0), (1, 0), (2, 0), (3, 0)],
        'J': [(0, 0), (0, 1), (1, 1), (2, 1)],
        'L': [(2, 0), (0, 1), (1, 1), (2, 1)],
        'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
        'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
        'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
        'T': [(1, 0), (0, 1), (1, 1), (2, 1)]
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plan_width = self.BLOCK_SIZE * 12
        self.plan_height = int(self.size[1] / 30) * 30
        self.pos_now = [0, 0]

    def update(self):
        self.draw_background()
        self.draw_item(self.ITEM['T'], self.pos_now)

    def event(self, event):
        if event.type in (KEYDOWN, KEYDOWN):
            if event.key == pygame.K_RIGHT:
                self.pos_now[0] += 1
            elif event.key == pygame.K_DOWN:
                self.pos_now[1] += 1
            elif event.key == pygame.K_LEFT:
                self.pos_now[0] -= 1
            elif event.key == pygame.K_UP:
                self.pos_now[1] -= 1

    def draw_background(self):
        self.screen.fill(BLACK)
        plan_margin = 15
        pygame.draw.rect(self.screen, WHITE, (
            (plan_margin, plan_margin), (self.plan_width - plan_margin * 2, self.plan_height - plan_margin * 2)
        ))
        plan_margin = 28
        pygame.draw.rect(self.screen, BLACK, (
            (plan_margin, plan_margin), (self.plan_width - plan_margin * 2, self.plan_height - plan_margin * 2)
        ))

    def draw_item(self, item, pos):
        for pos_offset in item:
            self.draw_block(pos, pos_offset)

    def draw_block(self, pos, pos_offset=(0, 0)):
        x, y = (pos[0] + pos_offset[0] + 1) * self.BLOCK_SIZE, (pos[1] + pos_offset[1] + 1) * self.BLOCK_SIZE
        pygame.draw.rect(self.screen, BLACK, (
            (x, y), (self.BLOCK_SIZE, self.BLOCK_SIZE)
        ))
        margin = 2
        pygame.draw.rect(self.screen, WHITE, (
            (x + margin, y + margin), (self.BLOCK_SIZE - margin * 2, self.BLOCK_SIZE - margin * 2)
        ))


tetris = Tetris([480, 640], "Tetris")
tetris.run_forever()
