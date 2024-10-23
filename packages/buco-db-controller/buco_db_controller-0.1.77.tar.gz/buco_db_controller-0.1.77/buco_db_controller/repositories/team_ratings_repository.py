import logging

from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

logger = logging.getLogger(__name__)


class TeamRatingsRepository(MongoDBBaseRepository):
    DB_NAME = 'sofifa'

    def __init__(self):
        super().__init__(self.DB_NAME)

    def upsert_many_team_ratings(self, odds):
        self.bulk_upsert_documents('team_ratings', odds)
        logger.info('Upsert team ratings data')

    def insert_team_ratings(self, odds):
        self.insert_document('team_ratings', odds)
        logger.info('Inserted team ratings data')

    def get_team_ratings(self, league_id: int, season: int) -> list:
        query = {'parameters.league': league_id, 'parameters.season': season}
        team_ratings = self.find_document('odds', query)
        logger.info(f'Fetching odds for league {league_id} for season {season}')
        return team_ratings
