from buco_db_controller.models.league import League
from buco_db_controller.models.team import Team


class Fixture:
    def __init__(
            self,
            fixture_id: int,
            datetime,
            status,

            league: League,
            season: int,
            league_round,

            home_team: Team,
            ht_winner,

            away_team: Team,
            at_winner,

            fulltime_goals,
            halftime_goals,
    ):
        self.fixture_id = fixture_id
        self.datetime = datetime
        self.status = status

        self.league = league
        self.season = season
        self.league_round = league_round

        self.home_team = home_team
        self.ht_winner = ht_winner

        self.away_team = away_team
        self.at_winner = at_winner

        self.fulltime_goals = fulltime_goals
        self.halftime_goals = halftime_goals

    @classmethod
    def from_dict(cls, data):
        return cls(
            fixture_id=data['fixture']['id'],
            datetime=data['fixture']['date'],
            status=data['fixture']['status'],
            league=League(
                league_id=data['league']['id'],
                name=data['league']['name'],
                country=data['league']['country']
            ),
            season=data['league']['season'],
            league_round=data['league']['round'],
            home_team=Team(
                team_id=data['teams']['home']['id'],
                name=data['teams']['home']['name'],
            ),
            ht_winner=data['teams']['home']['winner'],
            away_team=Team(
                team_id=data['teams']['away']['id'],
                name=data['teams']['away']['name'],
            ),
            at_winner=data['teams']['away']['winner'],
            fulltime_goals=data['score']['fulltime'],
            halftime_goals=data['score']['halftime'],
        )

    def get_fixture_date(self):
        return self.datetime.split('T')[0]
