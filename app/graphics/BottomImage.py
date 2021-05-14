import pygame


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
