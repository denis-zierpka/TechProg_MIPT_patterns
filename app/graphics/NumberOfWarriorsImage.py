import pygame


def number_of_chosen_warriors_image(screen, font, background, x, y, number, total):
    suffix = '/{}'.format(total)
    screen.fill(background, (x, y, x + font.size('0')[0] * 2, y + font.size('0')[1] * 2))
    screen.blit(font.render(str(number - 1) + suffix, True, background), (x, y))
    screen.blit(font.render(str(number) + suffix, True, (255, 0, 0)), (x, y))
    pygame.display.update()
