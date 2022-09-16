import arcade
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Гонка'


class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y


class Wall(arcade.Sprite):
    def __init__(self,):
        super(Wall, self).__init__('wall.png', 0.5)
        self.center_x = random.randint(100, 800)
        self.center_y = SCREEN_HEIGHT

    def update(self):
        self.center_y -= 10
        if self.center_y == 0:
            self.center_y = SCREEN_HEIGHT
            self.center_x = random.randint(100, 800)
            window.score += 1


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.car = Car('yellow_car.png',0.8)
        self.car.center_x = SCREEN_WIDTH / 2
        self.car.center_y = 75
        self.bg = arcade.load_texture('bg.png')
        self.wall = Wall()
        self.score = 0
        self.game = True
        self.lose = False

    def on_draw(self):
        self.clear((0,0,0))
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg)
        self.car.draw()
        self.wall.draw()
        arcade.draw_text(f'SCORE: {self.score} ', 100, 650,(255,255,255), 20)
        if self.score == 5:
            self.game = False
            arcade.draw_text('ВЫ ПОБЕДИЛИ', 350, 400,(153,255,51), 40)
        if self.lose == True:
            arcade.draw_text('ВЫ ПРОИГРАЛИ', 350, 400, (255,102,102), 40)

    def update(self, delta_time):
        if self.game:
            self.car.update()
            self.wall.update()
            if arcade.check_for_collision(self.car, self.wall):
                self.game = False
                self.lose = True

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.car.change_x = -5
            self.car.angle = 20
        if key == arcade.key.RIGHT:
            self.car.change_x = 5
            self.car.angle = -20


    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT or arcade.key.LEFT:
            self.car.change_x = 0
            self.car.angle = 0


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
