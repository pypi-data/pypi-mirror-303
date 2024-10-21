from buco_db_controller.models.xgoals import XGoals
from buco_db_controller.repositories.xgoals_repository import XGoalsRepository
from buco_db_controller.services.fixture_service import FixtureService


class XGoalsService:
    def __init__(self, db_name):
        self.xgoals_repository = XGoalsRepository(db_name)
        self.fixture_service = FixtureService()

    def upsert_many_fixture_xg(self, xgoals):
        self.xgoals_repository.upsert_many_fixture_xg(xgoals)

    def get_xgoals(self, fixture_id: int) -> XGoals:
        xgoals = self.xgoals_repository.get_xgoals(fixture_id)
        return xgoals

    def get_xgoals_over_season(self, team_id: int, league_id: int, season: int) -> list[XGoals]:
        fixture_ids = self.fixture_service.get_fixture_ids(team_id, league_id, season)
        xgoals_over_season = self.xgoals_repository.get_many_xgoals(fixture_ids)
        xgoals_over_season = [XGoals.from_dict(response) for response in xgoals_over_season]

        return xgoals_over_season
