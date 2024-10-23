

class Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name

    @classmethod
    def from_dict(cls, data):
        """
        Create a Team object from a dictionary.
        """
        return cls(
            team_id=data['team']['id'],
            name=data['team']['name'],
        )
