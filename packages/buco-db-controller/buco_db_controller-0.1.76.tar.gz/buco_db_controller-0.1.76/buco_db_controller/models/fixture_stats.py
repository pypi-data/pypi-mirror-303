

class FixtureStats:
    def __init__(
            self,
            fixture_id,
            home,
            away,
    ):
        self.fixture_id = fixture_id
        self.home = home
        self.away = away

    @classmethod
    def from_dict(cls, response):
        fixture_id = response['parameters']['fixture']

        home = response['data']['home']
        away = response['data']['away']

        return cls(
            fixture_id=fixture_id,
            home=home,
            away=away,
        )
