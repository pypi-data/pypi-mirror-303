import logging
from typing import List

from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

logger = logging.getLogger(__name__)


class InjuryRepository(MongoDBBaseRepository):
    DB_NAME = 'api_football'

    def __init__(self):
        super().__init__(self.DB_NAME)

    def upsert_many_injuries(self, injuries):
        self.bulk_upsert_documents('injuries', injuries)
        logger.info('Upsert fixture stats data')

    def get_injuries(self, fixture_id: int) -> list:
        query = {'parameters.fixture': fixture_id}
        injuries = self.find_document('injuries', query)
        logger.info(f'Fetching injuries for fixture {fixture_id}')
        return injuries

    def get_team_injuries(self, fixture_ids: List[int]) -> list:
        query = {'parameters.fixture': {'$in': fixture_ids}}
        injuries = self.find_documents('injuries', query)
        logger.info(f'Fetching lineups for fixtures {fixture_ids}')
        return injuries
