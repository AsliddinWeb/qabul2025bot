from enum import Enum, auto

class BotState(Enum):
    START = auto()

    ARIZA_TOPSHIRISH = auto()       # Telefon raqamni so'rash
    ARIZA_KOD = auto()              # 4 xonali kodni so'rash

    ARIZA_PASSPORT_SERIYA = auto() # Passport seriyasi
    ARIZA_TUGILGAN_SANA = auto()   # Tug'ilgan sana
    ARIZA_DAVLAT = auto()           # Davlat nomi
    ARIZA_VILOYAT = auto()          # Viloyat
    ARIZA_TUMAN = auto()            # Tuman
    ARIZA_FILIAL = auto()           # Filial
    ARIZA_TALIM_DARAJASI = auto()       # O'qish turi - magistr, bakalavr
    ARIZA_TALIM_SHAKLI = auto()     # Ta'lim shakli - sirtqi, kunduzgi
    ARIZA_YONALISH = auto()         # Yo'nalish

    UNIVERSITET_HAQIDA = auto()
    YONALISHLAR = auto()
    BOGLANISH = auto()
    DASTURCHI = auto()
