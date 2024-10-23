from buco_db_controller.models.team import Team


class Odds:
    def __init__(
            self,
            fixture_id: int,

            home_team: Team,
            away_team: Team,

            result,
            over_under,
            btts,
            dnb,
    ):
        self.fixture_id = fixture_id

        self.home_team = home_team
        self.away_team = away_team

        self.result = result
        self.over_under = over_under
        self.btts = btts
        self.dnb = dnb

    @classmethod
    def from_dict(cls, response):
        data = response['data']

        return cls(
            fixture_id=response['parameters']['fixture'],

            home_team=Team(
                team_id=data['home']['team']['id'],
                name=data['home']['team']['name'],
            ),
            away_team=Team(
                team_id=data['away']['team']['id'],
                name=data['away']['team']['name'],
            ),

            result=data['odds']['1X2'],
            over_under=data['odds']['over_under'],
            btts=data['odds']['btts'],
            dnb=data['odds']['dnb'],
        )
