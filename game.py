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
    BLOCK_SIZE = 28
    ITEM = {
        'I': [
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(1, 0), (1, 1), (1, 2), (1, 3)],
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(1, 0), (1, 1), (1, 2), (1, 3)],
        ],
        'J': [
            [(0, 0), (0, 1), (1, 1), (2, 1)],
            [(1, 0), (1, 1), (0, 2), (1, 2)],
            [(0, 0), (1, 0), (2, 0), (2, 1)],
            [(0, 0), (1, 0), (0, 1), (0, 2)],
        ],
        'L': [
            [(2, 0), (0, 1), (1, 1), (2, 1)],
            [(0, 0), (1, 0), (1, 1), (1, 2)],
            [(0, 0), (1, 0), (2, 0), (0, 1)],
            [(0, 0), (0, 1), (0, 2), (1, 2)],
        ],
        'O': [
            [(0, 0), (1, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (0, 1), (1, 1)],
        ],
        'S': [
            [(1, 0), (2, 0), (0, 1), (1, 1)],
            [(0, 0), (0, 1), (1, 1), (1, 2)],
            [(1, 0), (2, 0), (0, 1), (1, 1)],
            [(0, 0), (0, 1), (1, 1), (1, 2)],
        ],
        'Z': [
            [(0, 0), (1, 0), (1, 1), (2, 1)],
            [(1, 0), (0, 1), (1, 1), (0, 2)],
            [(0, 0), (1, 0), (1, 1), (2, 1)],
            [(1, 0), (0, 1), (1, 1), (0, 2)],
        ],
        'T': [
            [(1, 0), (0, 1), (1, 1), (2, 1)],
            [(1, 0), (0, 1), (1, 1), (1, 2)],
            [(0, 0), (1, 0), (2, 0), (1, 1)],
            [(0, 0), (0, 1), (1, 1), (0, 2)],
        ]
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plan_width = self.BLOCK_SIZE * 12
        self.plan_height = int(self.size[1] / self.BLOCK_SIZE) * self.BLOCK_SIZE
        self.pos_y_max = self.plan_height / self.BLOCK_SIZE - 2
        self.pos_x_max = self.plan_width / self.BLOCK_SIZE - 2
        self.pos_now = [0, 0]
        self.dir_now = 0
        self.block_fix = [(0, self.pos_y_max - 1), (self.pos_x_max - 1, self.pos_y_max - 1)]

    def update(self):
        self.draw_background()
        self.draw_fix_block()
        self.draw_item(self.ITEM['I'], self.pos_now, self.dir_now)

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
            elif event.key == pygame.K_SPACE:
                self.dir_now = self.dir_now + 1 if self.dir_now < 3 else 0

    def draw_background(self):
        self.screen.fill(BLACK)
        plan_margin = self.BLOCK_SIZE * 0.5
        pygame.draw.rect(self.screen, WHITE, (
            (plan_margin, plan_margin), (self.plan_width - plan_margin * 2, self.plan_height - plan_margin * 2)
        ))
        plan_margin = self.BLOCK_SIZE * 0.9
        pygame.draw.rect(self.screen, BLACK, (
            (plan_margin, plan_margin), (self.plan_width - plan_margin * 2, self.plan_height - plan_margin * 2)
        ))

    def draw_fix_block(self):
        for block_pos in self.block_fix:
            self.draw_block(block_pos)

    def draw_item(self, item, position, direction):
        for pos_offset in item[direction]:
            self.draw_block(position, pos_offset)

    def draw_block(self, pos, pos_offset=(0, 0)):
        x, y = (pos[0] + pos_offset[0] + 1) * self.BLOCK_SIZE, (pos[1] + pos_offset[1] + 1) * self.BLOCK_SIZE
        pygame.draw.rect(self.screen, BLACK, (
            (x, y), (self.BLOCK_SIZE, self.BLOCK_SIZE)
        ))
        margin = self.BLOCK_SIZE * 0.1
        pygame.draw.rect(self.screen, WHITE, (
            (x + margin, y + margin), (self.BLOCK_SIZE - margin * 2, self.BLOCK_SIZE - margin * 2)
        ))


tetris = Tetris([480, 640], "Tetris")
tetris.run_forever()
