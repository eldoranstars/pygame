class GameStats():
    def __init__(self):
        # Атрибуты класса
        self.ship_limit = 3
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ship_limit