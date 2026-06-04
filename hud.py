from direct.gui.OnscreenText import OnscreenText

class HUD:

    def __init__(self):

        self.health_text = OnscreenText(
            text="Health:100",
            pos=(-1.2,0.9),
            scale=0.05
        )

        self.gold_text = OnscreenText(
            text="Gold:0",
            pos=(-1.2,0.8),
            scale=0.05
        )

    def update_health(
        self,
        value
    ):

        self.health_text.setText(
            f"Health:{value}"
        )

    def update_gold(
        self,
        value
    ):

        self.gold_text.setText(
            f"Gold:{value}"
        )
