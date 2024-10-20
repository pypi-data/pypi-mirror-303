import logging
from typing import Optional

from buco_db_controller import League
from buco_db_controller.models.lineups import Lineups
from buco_db_controller.repositories.team_league_repository import TeamLeguesRepository
from buco_db_controller.repositories.lineups_repository import LineupsRepository
from buco_db_controller.services.fixture_service import FixtureService

LOGGER = logging.getLogger(__name__)


class TeamLeagueService:
    def __init__(self):
        self.team_league_service = TeamLeguesRepository()
        self.fixture_service = FixtureService()

    def upsert_many_team_leagues(self, fixture_lineups: list):
        self.team_league_service.bulk_upsert_documents('team_leagues', fixture_lineups)
        LOGGER.info('Upserted fixture stats data')

    def get_team_league(self, team_id: int, season: int) -> Optional[Lineups]:
        response = self.team_league_service.get_team_leagues(team_id, season)

        if not response.get('data', []):
            return None

        league = League.from_dict(response)
        return league
