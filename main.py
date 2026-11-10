from pico2d import * 
import game_framework
import logo_mode

open_canvas()
logo_mode.init()

# game loop
game_framework.run(logo_mode)
close_canvas() 