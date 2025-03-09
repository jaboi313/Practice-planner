from time import time

class Availability:
    def __init__(self, Monday:bool=True, Tuesday:bool=True, Wednesday:bool=True, Thursday:bool=True, Friday:bool=True, MondayStartTime:time=True, TuesdayStartTime:time=True, WednesdayStartTime:time=True, ThursdayStartTime:time=True, FridayStartTime:time=True):
        self.__Monday = Monday
        self.__Tuesday = Tuesday
        self.__Wednesday = Wednesday
        self.__Thursday = Thursday
        self.__Friday = Friday
        self.__MondayStartTime = MondayStartTime
        self.__TuesdayStartTime = TuesdayStartTime
        self.__WednesdayStartTime = WednesdayStartTime
        self.__ThursdayStartTime = ThursdayStartTime
        self.__FridayStartTime = FridayStartTime

    def SetAvailability(self, Monday:bool=True, Tuesday:bool=True, Wednesday:bool=True, Thursday:bool=True, Friday:bool=True, MondayStartTime:time=True, TuesdayStartTime:time=True, WednesdayStartTime:time=True, ThursdayStartTime:time=True, FridayStartTime:time=True):
        self.__Monday = Monday
        self.__Tuesday = Tuesday
        self.__Wednesday = Wednesday
        self.__Thursday = Thursday
        self.__Friday = Friday
        self.__MondayStartTime = MondayStartTime
        self.__TuesdayStartTime = TuesdayStartTime
        self.__WednesdayStartTime = WednesdayStartTime
        self.__ThursdayStartTime = ThursdayStartTime
        self.__FridayStartTime = FridayStartTime

    def GetAvailability(self):
        return self.__Monday, self.__Tuesday, self.__Wednesday, self.__Thursday, self.__Friday, self.__MondayStartTime, self.__TuesdayStartTime, self.__WednesdayStartTime, self.__ThursdayStartTime, self.__FridayStartTime