from direct.showbase.ShowBase import ShowBase

from player.player import Player
from world.game_world import GameWorld


class ShadowRealmChronicles(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        self.camera.setPos(0, -40, 15)
        self.camera.lookAt(0, 0, 0)

        self.world = GameWorld(self)
        self.world.load_world()

        self.player = Player(self)
        self.player.load_player()


game = ShadowRealmChronicles()
game.run()
