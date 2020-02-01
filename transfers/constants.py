import enum


class UserType(enum.Enum):
    STUDENT = 0
    AD = 1
    HOD = 2
    PSD = 3


class TransferType(enum.Enum):
    PS2TS = 0
    TS2PS = 1


class CampusType(enum.Enum):
	GOA = 0
	HYD = 1
	PILANI = 2
