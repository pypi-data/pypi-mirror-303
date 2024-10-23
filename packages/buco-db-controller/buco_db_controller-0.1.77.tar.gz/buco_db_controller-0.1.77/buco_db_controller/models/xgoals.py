from typing import Optional

from buco_db_controller.models.team import Team


class XGoals:
    def __init__(
            self,
            fixture_id,

            home_team: Team,
            away_team: Team,

            home_xg: Optional[float],
            away_xg: Optional[float],

            home_goals,
            away_goals
    ):
        self.fixture_id = fixture_id

        self.home_team = home_team
        self.away_team = away_team

        self.home_xg = float(home_xg) if home_xg else None
        self.away_xg = float(away_xg) if away_xg else None

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
