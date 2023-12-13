import random
from kaartspel import Kaart
class Speler:
    def __init__(self, naam:str, starterskapitaal:int):
        self._hand = []
        self.naam = naam
        self.geld = starterskapitaal
        self.bij=True           #Geeft aan of de speler is gepast of niet
        '''Constructor.
        :param naam: De naam van de speler. Ik weet nog niet of dit erg bruikbaar gaat zijn.
        :param starterskapitaal: beginnede hoeveelheid geld.'''

    @property
    def inHand(self)->tuple:
        '''Returnt tuple met kaarten in hand.'''
        return tuple(self._hand)

    def pak_kaarten(self,dek:list[Kaart])->list[Kaart]:  
        '''pakt 2 random kaarten en haalt die uit dek.
        :param dek: Het dek waar de kaart uit gepakt dient te worden
        :return: Returnt het dek zonder de kaarten die gepakt zijn'''
        self.kaart1 = random.choice(dek)  # raise error als dek te weinig kaarten heeft???
        dek.remove(self.kaart1)
        self.kaart2 = random.choice(dek)    #kaart1 & kaart2 zijn tijdelijke variabelen
        dek.remove(self.kaart2)
        self._hand.append(self.kaart1)
        self._hand.append(self.kaart2)
        return dek

    def leg_kaarten_terug(self,dek:list)->list:
        self.kaart1 = self._hand[0]
        self.kaart2 = self._hand[1]
        self._hand.clear()
        dek.append(self.kaart1)
        dek.append(self.kaart2)
        return dek

    def ontvang_pot(self,pot:int):
        self.geld+=pot
    def zet_in(self,inzet:int,pot:int)->int: #raise error als te weinig geld?
        self.geld-=inzet
        return pot+inzet
    @property
    def moneys(self)->int:
        return self.geld