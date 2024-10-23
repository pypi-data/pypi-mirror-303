

class Coefficients:
    def __init__(self, season, coefficients):
        self.season = season
        self.coefficients = coefficients

    @classmethod
    def from_dict(cls, response):
        return cls(season=response['parameters']['season'], coefficients=response['data'])
