class Kaart:
    def __init__(self, kleur, naam):
        self.kleur = kleur
        self.naam = naam

    def show(self):
        print(f"{self.kleur} {self.naam}")


if __name__ == '__main__':
    namen = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H", "A")
    kleuren = ("Harten", "Klaveren", "Ruiten", "Schoppen")
    kaarten = []
    for naam in namen:
        for kleur in kleuren:
            kaarten.append(Kaart(kleur, naam))
            # for kaart in kaarten:
            #     kaart.show()
