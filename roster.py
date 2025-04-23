from datetime import time, timedelta, datetime
from enum import Enum
from typing import List, Tuple


class Weekday(Enum):
    MA = 0
    DI = 1
    WO = 2
    DO = 3
    VR = 4
    ZA = 5
    ZO = 6


class TimeSlot:
    def __init__(self, day: Weekday, start: time, end: time):
        self.day = day
        self.start = start
        self.end = end

    def overlaps(self, other) -> bool:
        return self.day == other.day and not (self.end <= other.start or self.start >= other.end)


class Coach:
    def __init__(self, name: str, availability: List[TimeSlot], own_teams: List[str]):
        self.name = name
        self.availability = availability
        self.own_teams = own_teams


class Team:
    def __init__(self, name: str, sessions_per_week: int, session_length_minutes: int,
                 earliest_start: time, latest_end: time, coaches: List[str]):
        self.name = name
        self.sessions_per_week = sessions_per_week
        self.session_length = timedelta(minutes=session_length_minutes)
        self.earliest_start = earliest_start
        self.latest_end = latest_end
        self.coaches = coaches


class Field:
    def __init__(self, name: str, availability: List[TimeSlot]):
        self.name = name
        self.availability = availability


class Room:
    def __init__(self, name: str, fields: List[Field]):
        self.name = name
        self.fields = fields


def generate_schedule(teams: List[Team], coaches: List[Coach], rooms: List[Room]) -> List[Tuple[str, str, Weekday, time, time, str, str]]:
    schedule = []

    for team in teams:
        sessions_scheduled = 0
        eligible_coaches = [c for c in coaches if c.name in team.coaches]
        for coach in eligible_coaches:
            for day in Weekday:
                if sessions_scheduled >= team.sessions_per_week:
                    break

                for room in rooms:
                    for field in room.fields:
                        for coach_slot in coach.availability:
                            if coach_slot.day != day:
                                continue
                            for field_slot in field.availability:
                                if field_slot.day != day:
                                    continue

                                start = max(coach_slot.start, field_slot.start, team.earliest_start)
                                end = (datetime.combine(datetime.today(), start) + team.session_length).time()

                                if (end > team.latest_end or end > coach_slot.end or end > field_slot.end):
                                    continue

                                if team.name in coach.own_teams:
                                    continue

                                schedule.append((team.name, coach.name, day.name, start, end, room.name, field.name))
                                sessions_scheduled += 1

                                if sessions_scheduled >= team.sessions_per_week:
                                    break
                            if sessions_scheduled >= team.sessions_per_week:
                                break
                        if sessions_scheduled >= team.sessions_per_week:
                            break
                    if sessions_scheduled >= team.sessions_per_week:
                        break
    return schedule


# === Voorbeelddata ===
jeroen = Coach("Jeroen", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23))], own_teams=["Recreanten-m"])
davinia = Coach("Davinia", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=["VSE", "MSE"])
arjen = Coach("Arjen", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=[])
lorenzo = Coach("Lorenzo", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=[])
adik = Coach("Adik", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=[])
kelvin = Coach("Kelvin", [TimeSlot(Weekday.MA, time(18), time(23)), TimeSlot(Weekday.DI, time(18), time(23)), TimeSlot(Weekday.WO, time(18), time(23)), TimeSlot(Weekday.DO, time(18), time(23)), TimeSlot(Weekday.VR, time(18), time(23))], own_teams=["MSE"])
britt = Coach("Britt", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=["VSE"])
thomashoek = Coach("ThomasvH", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=["MSE"])
thomasbruns = Coach("ThomasB", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=["MSE"])
alex = Coach("Alex", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23))], own_teams=[])
thijs = Coach("Thijs", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23))], own_teams=[])
sharia = Coach("Sharia", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))], own_teams=["Recreanten-m"])

u10 = Team("U10", 2, 60, time(17), time(18), coaches=["Jeroen"])
m12 = Team("M12", 2, 90, time(18), time(20), coaches=["Sharia"])
v14 = Team("V14", 2, 90, time(18), time(20), coaches=["ThomasB"])
m14_3 = Team("M14-3", 2, 90, time(18), time(20), coaches=["Adik"])
m14_2 = Team("M14-2", 2, 90, time(18), time(20), coaches=["Arjen", "Lorenzo"])
m14_1 = Team("M14-1", 2, 90, time(18), time(20), coaches=["Davinia"])
v16 = Team("V16", 2, 90, time(18), time(22), coaches=["Britt"])
m16 = Team("M16", 2, 90, time(18), time(22), coaches=["Kelvin"])
v18 = Team("V18", 2, 90, time(18), time(23), coaches=["Adik"])
m18 = Team("M18", 2, 90, time(18), time(23), coaches=["ThomasvH"])
vse = Team("VSE", 2, 90, time(18), time(23), coaches=["Alex"])
mse = Team("MSE", 2, 90, time(18), time(23), coaches=["Thijs"])
recreanten_m = Team("Recreanten-m", 1, 90, time(21), time(23), coaches=[])

veld1 = Field("Beneden-L", [TimeSlot(Weekday.MA, time(18), time(21)), TimeSlot(Weekday.DI, time(18), time(21)), TimeSlot(Weekday.WO, time(18), time(21)), TimeSlot(Weekday.DO, time(18), time(21)), TimeSlot(Weekday.VR, time(18), time(21))])
veld2 = Field("Beneden-R", [TimeSlot(Weekday.MA, time(18), time(21)), TimeSlot(Weekday.DI, time(18), time(21)), TimeSlot(Weekday.WO, time(18), time(21)), TimeSlot(Weekday.DO, time(18), time(21)), TimeSlot(Weekday.VR, time(18), time(21))])
veld3 = Field("Boven-L", [TimeSlot(Weekday.MA, time(18), time(21)), TimeSlot(Weekday.DI, time(18), time(21)), TimeSlot(Weekday.WO, time(18), time(21)), TimeSlot(Weekday.DO, time(18), time(21)), TimeSlot(Weekday.VR, time(18), time(21))])
veld4 = Field("Boven-R", [TimeSlot(Weekday.MA, time(18), time(21)), TimeSlot(Weekday.DI, time(18), time(21)), TimeSlot(Weekday.WO, time(18), time(21)), TimeSlot(Weekday.DO, time(18), time(21)), TimeSlot(Weekday.VR, time(18), time(21))])
lariks = Room("de Lariks", [veld1, veld2, veld3, veld4])

veld1 = Field("Links", [TimeSlot(Weekday.MA, time(17), time(23)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))])
veld2 = Field("Rechts", [TimeSlot(Weekday.MA, time(17), time(18)), TimeSlot(Weekday.DI, time(17), time(23)), TimeSlot(Weekday.WO, time(17), time(23)), TimeSlot(Weekday.DO, time(17), time(23)), TimeSlot(Weekday.VR, time(17), time(23))])
spreng = Room("de Spreng", [veld1, veld2])

schedule = generate_schedule([u10, m12, v14, m14_3, m14_2, m14_1, v16, m16, v18, m18, vse, mse, recreanten_m], [jeroen, davinia, arjen, lorenzo, adik, kelvin, britt, thomashoek, thomasbruns, alex, thijs, sharia], [lariks, spreng])

for entry in schedule:
    print(f"Team {entry[0]} traint met Coach {entry[1]} op {entry[2]} van {entry[3]} tot {entry[4]} in {entry[5]} - {entry[6]}")
