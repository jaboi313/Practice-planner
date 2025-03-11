from Class.Coach import Coach
from Class.ID import TeamID

class Team:
    def __init__(self, TrainingAmount:int=2, AmountOfCoaches:int=1, *Coaches:Coach):
        self.__ID = TeamID
        self.__TrainingAmount = TrainingAmount
        self.__AmountOfCoaches = AmountOfCoaches

        if len(self.__Coaches) != self.__AmountOfCoaches:
            raise ValueError(f"You must provide exactly {self.__AmountOfCoaches} coaches. amount provided : {len(self.__Coaches)}")
        
        self.__Coaches = list(Coaches)

    def AddCoach(self, Coach:Coach):
        pass

    def RemoveCoach(self, CoachName:str=None, CoachID:int=None):
        pass