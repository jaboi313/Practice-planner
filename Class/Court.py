from Class.ID import CourtID
from typing import Tuple

class Court:
    def __init__(self, CourtType:str="Full", BasketAmount:int=2, Dimentions:Tuple[int,int]=(28,15)):
        self.__ID = CourtID()