from ClassAvailability import Availability
from ClassID import ID

class Coach:
    def __init__(self, Name:str, CoachTeam:str, PlayTeam:str=None, Availability:Availability=Availability()):
        self.__ID = ID()