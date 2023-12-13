class Kaart:
    def __init__(self, kleur:str, naam:str)->None:
        self._kleur = kleur
        self._naam = naam
        '''Constructor. Roep een kaart in het leven
        :param kleur: wat is de kleur van deze kaart? begin met een hoofdletter'''

    def show(self)->None:
        print(f"de {self._naam} van {self._kleur}")
        '''Deze method geeft de kleur en naar van de kaar'''
    @property
    def kleur(self)->str:
        '''Deze property returnt de kleur van de kaart'''
        return self._kleur
    @property
    def naam(self)->str:
        '''Deze property returnt de naam van een kaart. Naam in dit geval betekent de 2 of 4 of B.'''
        return self._naam

if __name__ == '__main__':
    namen = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H", "A")
    kleuren = ("Harten", "Klaveren", "Ruiten", "Schoppen")
    kaarten = []
    for naam in namen:
        for kleur in kleuren:
            kaarten.append(Kaart(kleur, naam))
            # for kaart in kaarten:
            #     kaart.show()
