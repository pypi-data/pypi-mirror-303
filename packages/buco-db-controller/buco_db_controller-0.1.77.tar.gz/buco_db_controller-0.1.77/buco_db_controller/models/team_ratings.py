from buco_db_controller.models.team import Team


class TeamRatings:
    def __init__(
            self,
            league,
            season,
            team_ratings
    ):
        self.league = league
        self.season = season
        self.team_ratings = team_ratings

    @classmethod
    def from_dict(cls, response):
        return cls(
            league=response['parameters']['league'],
            season=response['parameters']['season'],
            team_ratings=response['data']
        )
