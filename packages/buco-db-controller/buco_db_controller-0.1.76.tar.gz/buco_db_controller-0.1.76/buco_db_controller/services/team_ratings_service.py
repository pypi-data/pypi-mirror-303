from buco_db_controller.models.team_ratings import TeamRatings
from buco_db_controller.repositories.team_ratings_repository import TeamRatingsRepository


class TeamRatingsService:
    def __init__(self):
        self.team_ratings_repository = TeamRatingsRepository()

    def upsert_many_team_ratings(self, team_ratings):
        self.team_ratings_repository.upsert_many_team_ratings(team_ratings)

    def insert_team_ratings(self, team_ratings):
        self.team_ratings_repository.insert_team_ratings(team_ratings)

    def get_team_ratings(self, league_id: int, season: int) -> list[TeamRatings]:
        team_ratings = self.team_ratings_repository.get_team_ratings(league_id, season)
        team_ratings = [TeamRatings.from_dict(response) for response in team_ratings]
        return team_ratings
