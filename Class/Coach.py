from Class.Availability import Availability
from Class.ID import CoachID

class Coach:
    def __init__(self, Name:str, CoachTeam:str, PlayTeam:str=None, Availability:Availability=Availability()):
        self.__ID = CoachID()