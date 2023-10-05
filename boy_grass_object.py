from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):  # 생성자 함수 : 객체가 생성될 때, 맨 처음 자동 호출 되는 함수, 객체의 초기 상태를 설정 - 속성(멤버변수) 설정
        self.image = load_image('grass.png')

    def draw(self):  # self : 생성된 객체를 가리키는 더미 변수
        self.image.draw(400,30)

    def update(self): pass  # 전체적인 통일성을 위해 만들어 줌


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Small_ball:
    def  __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 20)
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.y >= 70:
            self.y -= random.randint(1, 7)
        else:
            False

    def draw(self):
        self.image.draw(self.x, self.y)


class Big_ball:
    def  __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.frame = random.randint(0, 20)
        self.image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.y >= 70:
            self.y -= random.randint(1, 7)
        else:
            False

    def draw(self):
        self.image.draw(self.x, self.y)
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
    global team
    global s_balls
    global b_balls
    global world

    running = True
    world = []  # 현재 게임 월드에 있는 객체를 모두 담고 있는 리스트
                # update_world 와 render_world 의 코드를 바꾸지 않아도 된다는 장점

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    s_balls = [Small_ball() for i in range(10)]
    world += s_balls

    b_balls = [Big_ball() for i in range(10)]
    world += b_balls


def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
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
