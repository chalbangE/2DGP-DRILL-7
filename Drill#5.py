from pico2d import *
import random

def load_resources():
    global TUK_ground, character, arrow
    TUK_ground = load_image('TUK_GROUND.png')
    character = load_image('animation_sheet.png')
    arrow = load_image('hand_arrow.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def reset_world():
    global running, cx, cy, frame, hx, hy, sx, sy, t, action
    running = True
    cx, cy = TUK_WIDTH // 2, TUK_HEIGHT // 2
    frame = 0
    action = 3
    sx, sy = cx, cy
    hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    t = 0.0
    set_new_target_arrow()

def set_new_target_arrow():
    global sx, sy, hx, hy, t
    sx, sy = cx, cy  # p1 : 시작점
    hx, hy = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)  # p2 : 끝점
    t = 0.0

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
hide_cursor()
load_resources()
reset_world()


def render_world():
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(hx, hy)
    character.clip_draw(frame * 100, 100 * action, 100, 100, cx, cy)
    update_canvas()


def update_world():
    global frame, cx, cy, t, action
    frame = (frame + 1) % 8
    action = 1 if cx < hx else 0

    if t <= 1.0:
        cx = (1 - t) * sx + t * hx  # cx 는 시작 x 와 끌 x 를 1-t:t 의 비율로 섞은 위치
        cy = (1 - t) * sy + t * hy
        t += 0.001
    else:
        cx, cy = hx, hy
        set_new_target_arrow()

while running:
    render_world()  # 월드의 현재 내용을 그린다
    handle_events()  # 사용자 입력받기
    update_world()  # 객체들의 상호작용을 계산하고 업데이트

close_canvas()
