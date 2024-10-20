from buco_db_controller.models.team import Team


class XGoals:
    def __init__(
            self,
            fixture_id,

            home_team: Team,
            away_team: Team,

            home_xg,
            away_xg,

            home_goals,
            away_goals
    ):
        self.fixture_id = fixture_id

        self.home_team = home_team
        self.away_team = away_team

        self.home_xg = home_xg
        self.away_xg = away_xg

        self.home_goals = home_goals
        self.away_goals = away_goals

    @classmethod
    def from_dict(cls, response):
        fixture_id = response['parameters']['fixture']
        data = response['data']

        return cls(
            fixture_id=fixture_id,

            home_team=Team(
                team_id=data['home']['team']['id'],
                name=data['home']['team']['name'],
            ),
            away_team=Team(
                team_id=data['away']['team']['id'],
                name=data['away']['team']['name'],
            ),

            home_xg=data['home']['statistics']['xg'],
            away_xg=data['away']['statistics']['xg'],

            home_goals=data['home']['statistics']['goals'],
            away_goals=data['away']['statistics']['goals']
        )
