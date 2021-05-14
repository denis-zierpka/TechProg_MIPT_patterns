import sys
import time

from app.FactoryRegister import Info
from app.graphics.BottomImage import ChooseBottomImage
from app.graphics.NumberOfWarriorsImage import number_of_chosen_warriors_image
from app.graphics.WarriorImage import WarriorImage
from app.warrior.Warrior import Warrior

import pygame


class GameGraphics:
    __this = None

    def __new__(cls, *args, **kwargs):
        if cls.__this is None:
            cls.__this = object.__new__(cls)
            return cls.__this

    def __init__(self):
        self.HEIGHT = 500
        self.WIDTH = 500
        self.BACKGROUND = pygame.Color('black')

        pygame.init()

        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.font = pygame.font.SysFont('Arial', 12, bold=True)
        self.big_font = pygame.font.SysFont('Arial', 24, bold=True)
        self.screen.fill(self.BACKGROUND)

    def choose_warriors(self, draw_object):
        total_number_of_warriors = len(Info.get_factories(Info))
        self.screen.fill(self.BACKGROUND)
        shift_top = 10
        shift_left = 10
        indent_between_objects = 10
        header = 'Choose warriors for {}'.format(draw_object)
        max_width, max_height = self.screen.get_size()
        word_width, word_height = self.big_font.size(header)

        self.screen.blit(
            self.big_font.render(header, True, pygame.Color('white')),
            (max_width // 2 - word_width // 2, shift_top)
        )
        shift_top += word_height + indent_between_objects
        pygame.display.update()

        warrior_images = []
        add_bottoms = []
        pop_bottoms = []
        for i in range(total_number_of_warriors):
            new_warrior_img = WarriorImage(self.BACKGROUND, shift_left, shift_top)
            new_add_bottom = ChooseBottomImage(
                new_warrior_img.center[0] +
                3 * new_warrior_img.radius +
                indent_between_objects,
                new_warrior_img.center[1]
            )
            new_pop_bottom = ChooseBottomImage(
                new_add_bottom.center[0] +
                new_add_bottom.radius +
                indent_between_objects,
                new_warrior_img.center[1]
            )
            warrior_images.append(new_warrior_img)
            add_bottoms.append(new_add_bottom)
            pop_bottoms.append(new_pop_bottom)
            shift_top += new_warrior_img.height
            shift_top += indent_between_objects

        result = {}
        for i, a, p, cls in zip(warrior_images, add_bottoms, pop_bottoms, Info.get_factories(Info)):
            i.draw(self.screen, self.font, str(cls))
            a.draw(self.screen, self.font, '+')
            p.draw(self.screen, self.font, '-')
            result[str(cls)] = 0

        number_of_chosen_warriors_image(
            self.screen,
            self.big_font,
            self.BACKGROUND,
            shift_left,
            shift_top,
            0,
            total_number_of_warriors
        )
        number_of_chosen = 0
        while True:
            time.sleep(0.05)
            if number_of_chosen == total_number_of_warriors:
                print(result)
                self.screen.fill(color=pygame.Color('red'))
                pygame.display.update()
                return result
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    click = pygame.mouse.get_pos()

                    for cls, i, j in zip(Info.get_factories(Info), add_bottoms, pop_bottoms):
                        if j.is_clicked(click[0], click[1]) and result[str(cls)] > 0:
                            result[str(cls)] -= 1
                            number_of_chosen -= 1
                        if i.is_clicked(click[0], click[1]):
                            result[str(cls)] += 1
                            number_of_chosen += 1

                    number_of_chosen_warriors_image(
                        self.screen,
                        self.big_font,
                        self.BACKGROUND,
                        shift_left,
                        shift_top,
                        number_of_chosen,
                        total_number_of_warriors
                    )
