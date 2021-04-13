import sys
import time
from app.warrior.Warrior import Warrior

import pygame


class GameGraphicsAdapter:
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

    def choose_warriors(self, player):
        total_number_of_warriors = len(Warrior.__subclasses__())
        self.screen.fill(self.BACKGROUND)
        shift_top = 10
        shift_left = 10
        indent_between_objects = 10
        header = 'Choose warriors for {}'.format(player)
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
        for i, a, p, cls in zip(warrior_images, add_bottoms, pop_bottoms, Warrior.__subclasses__()):
            i.draw(self.screen, self.font, str(cls.__name__))
            a.draw(self.screen, self.font, '+')
            p.draw(self.screen, self.font, '-')
            result[str(cls.__name__)] = 0

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
                    for cls, i, j in zip(Warrior.__subclasses__(), add_bottoms, pop_bottoms):
                        if j.is_clicked(click[0], click[1]) and result[str(cls.__name__)] > 0:
                            result[str(cls.__name__)] -= 1
                            number_of_chosen -= 1
                        if i.is_clicked(click[0], click[1]):
                            result[str(cls.__name__)] += 1
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


class WarriorImage:
    def __init__(self, background, x, y):
        self.radius = 40
        self.height = 2 * self.radius
        self.length = 2 * self.radius
        self.center = (x + self.radius, y + self.radius)
        self.x = x
        self.y = y
        self.background = background

    def draw(self, screen, font, name, color=(255, 255, 255)):
        pygame.draw.circle(
            screen,
            color,
            (self.x + self.radius, self.y + self.radius),
            self.radius
        )
        word_width, word_height = font.size(name)
        screen.blit(
            font.render(name, True, (255, 0, 0)),
            (self.x + self.radius - word_width // 2, self.y + self.radius - word_height // 2)
        )
        pygame.display.update()

    def erase(self, screen):
        pygame.draw.circle(
            screen,
            self.background,
            (self.x + self.radius, self.y + self.radius),
            self.radius
        )
        pygame.display.update()


class ChooseBottomImage:
    def __init__(self, x, y):
        self.radius = 20
        self.height = 2 * self.radius
        self.length = 2 * self.radius
        self.center = (x + self.radius, y)
        self.x = x
        self.y = y

    def draw(self, screen, font, text, color=(255, 255, 255)):
        word_width, word_height = font.size(text)
        pygame.draw.circle(
            screen,
            color,
            (self.x + self.radius, self.y),
            self.radius
        )

        screen.blit(
            font.render(text, True, (0, 0, 0)),
            (self.x + self.radius - word_width // 2, self.y - word_height // 2)
        )
        pygame.display.update()

    def is_clicked(self, x, y):
        return (x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 <= self.radius ** 2


def number_of_chosen_warriors_image(screen, font, background, x, y, number, total):
    suffix = '/{}'.format(total)
    screen.fill(background, (x, y, x + font.size('0')[0] * 2, y + font.size('0')[1] * 2))
    screen.blit(font.render(str(number - 1) + suffix, True, background), (x, y))
    screen.blit(font.render(str(number) + suffix, True, (255, 0, 0)), (x, y))
    pygame.display.update()


def test():
    it = GameGraphicsAdapter()
    it.choose_warriors("NIKITA")
