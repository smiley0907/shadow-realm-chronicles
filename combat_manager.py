class CombatManager:

    def __init__(self):

        self.player_damage = 10

    def attack_enemy(
        self,
        enemy
    ):

        enemy.take_damage(
            self.player_damage
        )
