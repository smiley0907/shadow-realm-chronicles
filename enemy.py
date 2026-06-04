class Enemy:

    def __init__(self, base):

        self.base = base

        self.enemy = None

        self.health = 50

    def spawn_enemy(self, x, y, z):

        self.enemy = self.base.loader.loadModel(
            "models/panda"
        )

        self.enemy.reparentTo(
            self.base.render
        )

        self.enemy.setScale(
            0.3
        )

        self.enemy.setPos(
            x,
            y,
            z
        )

        return self.enemy

    def take_damage(self, damage):

        self.health -= damage

        print(
            f"Enemy Health: {self.health}"
        )

        if self.health <= 0:

            self.enemy.removeNode()
