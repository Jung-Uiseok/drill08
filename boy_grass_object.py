from pico2d import *


# Game object class here
class Grass:
    def __init__(self):  # 생성자 함수 : 객체가 생성될 때, 맨 처음 자동 호출 되는 함수, 객체의 초기 상태를 설정 - 속성(멤버변수) 설정
        self.image = load_image('grass.png')

    def draw(self):  # self : 생성된 객체를 가리키는 더미 변수
        self.image.draw(400,30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()


def reset_world():
    global running
    global grass
    global boy
    global team

    running = True
    grass = Grass()
    boy = Boy()
    team = [Boy() for i in range(10)]


def update_world():
    grass.update()
    for boy in team:
        boy.update()


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()


# initialization code
reset_world()
# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)
# finalization code

close_canvas()
