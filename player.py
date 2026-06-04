from direct.task import Task
self.health = 100

self.gold = 0

class Player:

    def __init__(self, base):

        self.base = base

        self.player = None

        self.speed = 0.5

    def load_player(self):

        self.player = self.base.loader.loadModel(
            "models/panda"
        )

        self.player.reparentTo(
            self.base.render
        )

        self.player.setScale(0.5)

        self.player.setPos(
            0,
            0,
            0
        )

        self.register_keys()

    def register_keys(self):

        self.base.accept(
            "arrow_up",
            self.move_forward
        )

        self.base.accept(
            "arrow_down",
            self.move_backward
        )

        self.base.accept(
            "arrow_left",
            self.move_left
        )

        self.base.accept(
            "arrow_right",
            self.move_right
        )

    def move_forward(self):
        self.player.setY(
            self.player.getY() + self.speed
        )

    def move_backward(self):
        self.player.setY(
            self.player.getY() - self.speed
        )

    def move_left(self):
        self.player.setX(
            self.player.getX() - self.speed
        )

    def move_right(self):
        self.player.setX(
            self.player.getX() + self.speed
        )
