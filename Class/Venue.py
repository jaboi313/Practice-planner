from Class.VenueID import VenueID
from Class.Availability import Availability

class Venue:
    def __init__(self, CourtAmount:int=2, Availability:Availability=Availability()):
        self.__ID = VenueID()
        self.__CourtAmount = CourtAmount
        self.__Availability = Availability