from typing import List

from buco_db_controller.models.fixture import Fixture
from buco_db_controller.repositories.fixture_repository import FixtureRepository


class FixtureService:

    def __init__(self):
        self.fixture_repository = FixtureRepository()

    def upsert_many_fixtures(self, fixtures: List[dict]):
        self.fixture_repository.upsert_many_fixtures(fixtures)

    def get_team_fixtures(self, team_id: int, league_id: int, seasons) -> List[Fixture]:
        seasons = [seasons] if isinstance(seasons, int) else seasons
        response = self.fixture_repository.get_team_fixtures(team_id, league_id, seasons)
        fixtures_data = response.get('data', [])

        if not fixtures_data:
            raise ValueError(f'No fixtures found for team {team_id}, league {league_id} and season {season}')

        fixtures = [Fixture.from_dict(team) for team in fixtures_data]
        fixtures.sort(key=lambda x: x.datetime)
        return fixtures

    def get_league_fixtures(self, league_id: int, season: int) -> List[Fixture]:
        response = self.fixture_repository.get_league_fixtures(league_id, season)
        fixtures_data = [fixture for team in response for fixture in team.get('data', [])]
        fixtures_data = list({fixture['fixture']['id']: fixture for fixture in fixtures_data}.values())

        if not fixtures_data:
            raise ValueError(f'No fixtures found league {league_id} and season {season}')

        fixtures = [Fixture.from_dict(team) for team in fixtures_data]
        fixtures.sort(key=lambda x: (x.datetime, x.fixture_id))
        return fixtures

    def get_fixture_ids(self, team_id: int, league_id: int, seasons) -> list:
        seasons = [seasons] if isinstance(seasons, int) else seasons
        fixtures = self.fixture_repository.get_team_fixtures(team_id, league_id, seasons)
        fixture_ids = [fixture['fixture']['id'] for fixture in fixtures['data']]
        fixture_ids.sort()
        return fixture_ids

    def get_league_fixture_ids(self, league_id: int, season: int) -> list:
        fixtures = self.fixture_repository.get_league_fixtures(league_id, season)
        fixture_ids = [fixture['fixture']['id'] for team in fixtures for fixture in team['data']]
        fixture_ids.sort()
        return fixture_ids

    def get_fixture_dates(self, team_id: int, league_id: int, season: int) -> list:
        fixtures = self.fixture_repository.get_team_fixtures(team_id, league_id, season)
        fixture_dates = [fixture['fixture']['date'] for fixture in fixtures['data']]
        return fixture_dates

    def get_fixture_by_round(self, league_round: str, team_id: int, league_id: int, season: int) -> Fixture:
        fixtures = self.fixture_repository.get_team_fixtures(team_id, league_id, season)

        for fixture in fixtures['data']:
            if fixture['league']['round'] == league_round:
                return Fixture.from_dict(fixture)

        raise ValueError(f'No fixture found for round {league_round} | team {team_id} | league {league_id} | season {season}')

    def upsert_many_rounds(self, league_rounds):
        self.fixture_repository.upsert_many_rounds(league_rounds)

    def get_number_of_rounds(self, league_id: int, season: int) -> int:
        league_rounds = self.fixture_repository.get_rounds(league_id, season)
        league_rounds = [league_round for league_round in league_rounds['data'] if 'Regular Season' in league_round]
        return len(league_rounds)

    def get_league_rounds(self, league_id: int, season: int) -> list:
        league_rounds = self.fixture_repository.get_rounds(league_id, season)
        league_rounds = [league_round for league_round in league_rounds['data'] if 'Regular Season' in league_round]
        return league_rounds

    def get_fixture(self, fixture_id):
        response = self.fixture_repository.get_fixture(fixture_id)
        fixture = Fixture.from_dict(response['data'])
        return fixture

