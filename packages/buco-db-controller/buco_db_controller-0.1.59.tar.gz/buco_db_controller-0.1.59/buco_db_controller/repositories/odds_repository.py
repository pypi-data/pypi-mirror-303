import logging

from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

logger = logging.getLogger(__name__)


class OddsRepository(MongoDBBaseRepository):

    def __init__(self, db_name):
        super().__init__(db_name)

    def upsert_many_odds(self, odds):
        self.bulk_upsert_documents('odds', odds)
        logger.info('Upsert odds data')

    def insert_odds(self, odds):
        self.insert_document('odds', odds)
        logger.info('Inserted odds data')

    def get_odds(self, fixture_id: int, league_id: int, season: int) -> list:
        query = {'parameters.fixture': fixture_id, 'parameters.league': league_id, 'parameters.season': season}
        odds = self.find_document('odds', query)
        logger.info(f'Fetching odds for league {league_id} for season {season}')
        return odds

    def get_team_odds(self, fixture_ids: list) -> list:
        query = {'parameters.fixture': {'$in': fixture_ids}}
        odds = self.find_documents('odds', query)
        logger.info(f'Fetching xgoals for fixtures {fixture_ids}')
        return odds

    def get_league_odds(self, league_id: int, season: int) -> list:
        query = {'parameters.league': league_id, 'parameters.season': season}
        odds = self.find_documents('odds', query)
        logger.info(f'Fetching odds for league {league_id} for season {season}')
        return odds
