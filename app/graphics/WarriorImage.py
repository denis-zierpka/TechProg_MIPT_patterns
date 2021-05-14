import pygame


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
