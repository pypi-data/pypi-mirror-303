from typing import Union, List

from buco_db_controller.models.team import Team
from buco_db_controller.models.teams_stats import TeamStats
from buco_db_controller.repositories.fixture_repository import FixtureRepository
from buco_db_controller.repositories.team_repository import TeamRepository


class TeamService:
    def __init__(self):
        self.team_repository = TeamRepository()
        self.fixture_repository = FixtureRepository()

    def upsert_many_teams(self, teams: List[dict]):
        self.team_repository.upsert_many_teams(teams)

    def get_teams(self, league_id: int, season: int) -> List[Team]:
        response = self.team_repository.get_teams(league_id, season)

        if not response.get('data', []):
            raise ValueError(f'No teams found for league {league_id} and season {season}')

        teams = [Team.from_dict(team) for team in response['data']]
        return teams

    def get_team_ids(self, league_id: int, seasons: Union[int, List[int]]) -> List[int]:
        teams_over_seasons = self.team_repository.get_many_teams(league_id, seasons)

        team_ids = []
        for teams in teams_over_seasons:
            team_ids.extend([team['team']['id'] for team in teams['data']])

        team_ids = list(map(int, set(team_ids)))
        team_ids.sort()
        return team_ids

    def count_consecutive_years_in_league(self, team_id: int, league_id: int, current_season: int) -> int:
        seasons_to_check = list(range(2014, current_season + 1))
        consecutive_years_in_league = 0

        for season in seasons_to_check:
            fixtures = self.fixture_repository.get_team_fixtures(team_id, league_id, season)

            if fixtures and fixtures['data'][0]['league']['id'] == league_id:
                consecutive_years_in_league += 1
            else:
                consecutive_years_in_league = 0

        return consecutive_years_in_league
