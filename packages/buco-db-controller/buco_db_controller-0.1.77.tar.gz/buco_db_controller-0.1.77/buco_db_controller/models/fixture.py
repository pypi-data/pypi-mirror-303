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

            ht: Team,
            ht_winner: bool,

            at: Team,
            at_winner: bool,

            ft_goals,
            mt_goals,
    ):
        self.fixture_id = fixture_id
        self.datetime = datetime
        self.status = status

        self.league = league
        self.season = season
        self.league_round = league_round

        self.ht = ht
        self.ht_winner = ht_winner

        self.at = at
        self.at_winner = at_winner

        self.ft_goals = ft_goals
        self.mt_goals = mt_goals

    @classmethod
    def from_dict(cls, data) -> 'Fixture':
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
            ht=Team(
                team_id=data['teams']['home']['id'],
                name=data['teams']['home']['name'],
            ),
            ht_winner=data['teams']['home']['winner'],
            at=Team(
                team_id=data['teams']['away']['id'],
                name=data['teams']['away']['name'],
            ),
            at_winner=data['teams']['away']['winner'],
            ft_goals=data['score']['fulltime'],
            mt_goals=data['score']['halftime'],
        )

    def get_fixture_date(self):
        return self.datetime.split('T')[0]
