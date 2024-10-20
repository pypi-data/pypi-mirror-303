from buco_db_controller.models.team import Team


class TeamLineups:
    def __init__(
            self,
            team,
            startXI,
            substitutes,
            formation
    ):
        self.team = team
        self.startXI = startXI
        self.substitutes = substitutes
        self.formation = formation

    @classmethod
    def from_dict(cls, data):
        return cls(
            team=Team(
                team_id=data['team']['id'],
                name=data['team']['name']
            ),
            startXI=data['startXI'],
            substitutes=data['substitutes'],
            formation=data['formation']
        )
