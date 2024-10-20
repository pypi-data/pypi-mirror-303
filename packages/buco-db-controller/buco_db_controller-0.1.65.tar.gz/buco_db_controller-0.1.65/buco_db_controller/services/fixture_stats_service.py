from typing import List

from buco_db_controller.models.fixture_stats import FixtureStats
from buco_db_controller.repositories.fixture_stats_repository import FixtureStatsRepository
from buco_db_controller.services.fixture_service import FixtureService


class FixtureStatsService:
    def __init__(self, db_name):
        self.fixture_stats_repository = FixtureStatsRepository(db_name)
        self.fixture_service = FixtureService()

    def upsert_many_fixture_stats(self, fixture_stats: List[dict]):
        self.fixture_stats_repository.upsert_many_fixture_stats(fixture_stats)

    def get_fixture_stats(self, fixture_id: int) -> FixtureStats:
        response = self.fixture_stats_repository.get_fixture_stats(fixture_id)

        if not response.get('data', []):
            raise ValueError(f'No fixture stats found for fixture {fixture_id}')

        fixture_stats = FixtureStats.from_dict(response)
        return fixture_stats

    def get_fixture_stats_over_season(self, team_id: int, league_id: int, season: int) -> List[FixtureStats]:
        fixture_ids = self.fixture_service.get_fixture_ids(team_id, league_id, season)
        fixture_stats = self.fixture_stats_repository.get_team_fixture_stats(fixture_ids)
        fixture_stats = [FixtureStats.from_dict(fixture_stat) for fixture_stat in fixture_stats]
        return fixture_stats
