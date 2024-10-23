from datetime import datetime

from buco_db_controller.models.league import League


class TeamStats:
    def __init__(
            self,
            fixture_id,
            season,
            date,
            league,
            team_id,
            league_round,
            team_stats,
    ):
        self.fixture_id = fixture_id
        self.date = date
        self.season = season
        self.team_id = team_id
        self.league = league
        self.league_round = league_round
        self.team_stats = team_stats

    @classmethod
    def from_dict(cls, response):
        fixture_id = response['parameters']['fixture']

        date = response['parameters']['date']
        season = response['parameters']['season']
        league_round = response['parameters']['round']
        team_id = response['parameters']['team']

        data = response['data']

        return cls(
            fixture_id=fixture_id,
            season=season,
            date=datetime.strptime(date, '%Y-%m-%d'),
            league=League(
                league_id=data['league']['id'],
                name=data['league']['name']
            ),
            league_round=league_round,
            team_id=team_id,
            team_stats=data,
        )
