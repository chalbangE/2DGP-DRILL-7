from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def load_resources():
    global TUK_ground, character
    global arrow

    arrow = load_image('hand_arrow.png')
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')


def handle_events():
    global running, mx, my
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def reset_world():
    global running, cx, cy, frame, mx, my, t, action, points

    mx, my = 0, 0
    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3
    points = [(100, 900), (1200, 800), (500, 100)]

def set_new_target_arrow():
    global sx, sy, hx, hy, t
    global action
    global frame
    sx, sy = cx, cy
    hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)  # p2 : 끝점.
    t = 0.0
    action = 1 if sx < hx else 0
    frame = 0


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    for p in points:
        arrow.draw(p[0], p[1])
    arrow.draw(mx, my)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame
    global cx, cy
    global t

    frame = (frame + 1) % 8

open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()

while running:
    render_world()
    handle_events()
    update_world()

close_canvas()