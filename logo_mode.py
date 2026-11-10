from pico2d import * 
import game_framework
import tile_mode

image = None
running = True
logo_start_time = 0.0

def init():
    global image, logo_start_time
    global running
    image = load_image('tuk_credit.png')
    running = True
    logo_start_time = get_time()
    pass

def finish():
    global image
    del image
    pass

def update():
    global running, logo_start_time
    if get_time() - logo_start_time >= 2.0:
        game_framework.change_mode(tile_mode)
    pass

def render():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass
