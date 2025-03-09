from ClassCoach import Coach

class Team:
    def __init__(self, Coach:Coach, AssistantCoach:Coach, TrainingAmount:int):
        self.__Coach = Coach
        self.__AssistantCoach = AssistantCoach
        self.__TrainingAmount = TrainingAmount