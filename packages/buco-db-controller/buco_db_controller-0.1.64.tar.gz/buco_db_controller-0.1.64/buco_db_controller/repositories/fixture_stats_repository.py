import logging
from typing import List

from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

logger = logging.getLogger(__name__)


class FixtureStatsRepository(MongoDBBaseRepository):
    def __init__(self, db_name):
        super().__init__(db_name)

    def upsert_many_fixture_stats(self, fixture_stats):
        self.bulk_upsert_documents('fixtures_stats', fixture_stats)
        logger.info('Upserted fixture stats data')

    def get_fixture_stats(self, fixture_id: int) -> dict:
        query = {'parameters.fixture': fixture_id}
        stats = self.find_document('fixtures_stats', query)
        logger.info(f'Fetching stats for fixture {fixture_id}')
        return stats

    def get_team_fixture_stats(self, fixture_ids: List[int]) -> list:
        query = {'parameters.fixture': {'$in': fixture_ids}}
        fixture_stats = self.find_documents('fixtures_stats', query)
        logger.info(f'Fetching lineups for fixtures {fixture_ids}')
        return fixture_stats
