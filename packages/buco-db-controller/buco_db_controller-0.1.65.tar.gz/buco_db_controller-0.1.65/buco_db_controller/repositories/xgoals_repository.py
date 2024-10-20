import logging
from typing import List, Union

from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

LOGGER = logging.getLogger(__name__)


class XGoalsRepository(MongoDBBaseRepository):

    def __init__(self, db_name):
        super().__init__(db_name)

    def upsert_many_fixture_xg(self, xg):
        self.bulk_upsert_documents('xgoals', xg)
        LOGGER.info('Upserted fixture xgoals data')

    def get_xgoals(self, fixture_id: int) -> list:
        query = {'parameters.fixture': fixture_id}
        xg = self.find_document('xgoals', query)
        LOGGER.info(f'Fetching xgoals for fixture {fixture_id}')
        return xg

    def get_many_xgoals(self, fixture_ids: List[int]) -> list:
        query = {'parameters.fixture': {'$in': fixture_ids}}
        xg = self.find_documents('xgoals', query)
        LOGGER.info(f'Fetching fbref xgoals for fixtures {fixture_ids}')
        return xg
