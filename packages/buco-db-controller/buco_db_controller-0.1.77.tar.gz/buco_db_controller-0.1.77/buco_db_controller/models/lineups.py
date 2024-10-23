from buco_db_controller.models.team_lineups import TeamLineups


class Lineups:
    def __init__(
            self,
            fixture_id,
            ht_lineup,
            at_lineup
    ):
        self.fixture_id = fixture_id
        self.ht_lineup = ht_lineup
        self.at_lineup = at_lineup

    @classmethod
    def from_dict(cls, response):
        fixture_id = response['parameters']['fixture']
        data = response['data']

        home_team_injuries = TeamLineups.from_dict(data[0])
        away_team_injuries = TeamLineups.from_dict(data[1])

        return cls(
            fixture_id=fixture_id,
            ht_lineup=home_team_injuries,
            at_lineup=away_team_injuries
        )
