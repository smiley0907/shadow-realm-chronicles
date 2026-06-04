class SoundManager:

    def __init__(
        self,
        base
    ):

        self.base = base

    def play_background_music(self):

        music = self.base.loader.loadSfx(
            "assets/audio/background.ogg"
        )

        music.setLoop(True)

        music.play()

    def play_attack_sound(self):

        attack = self.base.loader.loadSfx(
            "assets/audio/sword.ogg"
        )

        attack.play()
