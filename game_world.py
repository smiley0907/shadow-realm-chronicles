class GameWorld:

    def __init__(self, base):

        self.base = base

    def load_world(self):

        world = self.base.loader.loadModel(
            "models/environment"
        )

        world.reparentTo(
            self.base.render
        )

        world.setScale(
            0.1
        )

        world.setPos(
            -8,
            42,
            0
        )
