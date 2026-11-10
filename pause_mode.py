from math import sqrt

from pico2d import *
import game_framework
import game_world


def init():
    pass


def finish():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return
        elif event.type == SDL_KEYUP:
            game_framework.stack[-2].boy.handle_event(event)


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    x, y = get_canvas_width() / 2, get_canvas_height() / 2
    radius = 80
    draw_circle(x, y, radius, 0, 0, 0, filled=True)
    width = radius * 1.5
    left = x - radius / 2
    for offset in range(int(width) + 1):
        half_height = (width - offset) / sqrt(3)
        draw_line(left + offset, y - half_height,
                  left + offset, y + half_height, 255, 255, 255)
    update_canvas()
