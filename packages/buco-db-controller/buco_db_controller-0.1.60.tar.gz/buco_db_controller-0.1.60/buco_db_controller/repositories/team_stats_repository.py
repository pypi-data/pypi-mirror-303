import logging
from typing import List

from buco_db_controller.mongo_db.mongo_db_repository import MongoDBBaseRepository

logger = logging.getLogger(__name__)


class TeamStatsRepository(MongoDBBaseRepository):
    DB_NAME = 'api_football'

    def __init__(self):
        super().__init__(self.DB_NAME)

    def upsert_many_team_stats(self, team_stats: List[dict]):
        self.bulk_upsert_documents('teams_stats', team_stats)
        logger.info('Upserted team stats data')

    def get_team_stats(self, team_id, league, seasons) -> List[dict]:
        seasons = [int(season) for season in seasons]
        query = {'parameters.team': team_id, 'parameters.league': league, 'parameters.season': {'$in': seasons}}
        team_stats = self.find_documents('teams_stats', query)
        logger.info(f'Fetching stats for team {team_id} for league {league} for seasons {seasons}')
        return team_stats
