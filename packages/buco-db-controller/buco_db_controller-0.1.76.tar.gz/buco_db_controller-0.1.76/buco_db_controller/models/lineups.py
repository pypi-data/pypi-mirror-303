from buco_db_controller.models.team_lineups import TeamLineups


class Lineups:
    def __init__(
            self,
            fixture_id,
            home_team_injuries,
            away_team_injuries
    ):
        self.fixture_id = fixture_id
        self.home_team_injuries = home_team_injuries
        self.away_team_injuries = away_team_injuries

    @classmethod
    def from_dict(cls, response):
        fixture_id = response['parameters']['fixture']
        data = response['data']

        home_team_injuries = TeamLineups.from_dict(data[0])
        away_team_injuries = TeamLineups.from_dict(data[1])

        return cls(
            fixture_id=fixture_id,
            home_team_injuries=home_team_injuries,
            away_team_injuries=away_team_injuries
        )
