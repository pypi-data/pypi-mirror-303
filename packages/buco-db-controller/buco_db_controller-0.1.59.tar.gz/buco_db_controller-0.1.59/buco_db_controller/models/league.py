
class League:
    def __init__(self, league_id, name, country=None):
        self.league_id = league_id
        self.name = name
        self.country = country

    @classmethod
    def from_dict(cls, response):
        data = response['data']
        return cls(
            league_id=data[-1]['league']['id'],
            name=data[-1]['league']['name'],
            country=data[-1]['country']['name']
        )
