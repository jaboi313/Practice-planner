class ID:
    _Counter = 1

    def __init__(self):
        self.ID = ID._Counter
        ID._Counter += 1

    def ResetCounter(self):
        self._Counter = 1

    def SetCounter(self, Value:int):
        self._Counter = Value

class CoachID(ID):
    super.__init__()

class CourtID(ID):
    super.__init__()

class TeamID(ID):
    super.__init__()

class VenueID(ID):
    super.__init__()