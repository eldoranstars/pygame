class GameStats():
    def __init__(self, settings):
        # Атрибуты класса
        self.settings = settings
        self.reset_stats()
        self.game_status = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit