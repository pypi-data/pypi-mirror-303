import logging
from typing import List, Union

from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

logger = logging.getLogger(__name__)


class TeamLeguesRepository(MongoDBBaseRepository):
    DB_NAME = 'api_football'

    def __init__(self):
        super().__init__(self.DB_NAME)

    def upsert_many_team_leagues(self, lineups: List[dict]):
        self.bulk_upsert_documents('team_leagues', lineups)
        logger.info('Upserted fixture lineups data')

    def get_team_leagues(self, team_id: int, season: int) -> list:
        query = {'parameters.team': team_id, 'parameters.season': season}
        lineups = self.find_document('team_leagues', query)
        return lineups
