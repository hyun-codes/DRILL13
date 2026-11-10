from pico2d import *
import game_framework
import game_world
import tile_mode
import pause_mode
from boy import Boy
from grass import Grass


def handle_events():
    global item_window_open
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(tile_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_window_open = not item_window_open
        else:
            boy.handle_event(event)



def init():
    global boy, item_image, item_window_open

    item_image = load_image('item_select.png')
    item_window_open = False

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def pause():
    global pause_started_at
    pause_started_at = get_time()


def resume():
    boy.idle_started_at += get_time() - max(pause_started_at, boy.idle_started_at)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if item_window_open:
        item_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()

def finish():
    game_world.clear()


