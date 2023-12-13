import unittest
from speler import Speler
from kaartspel import Kaart


NAMEN = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H", "A")
KLEUREN = ("Harten", "Klaveren", "Ruiten", "Schoppen")
def maak_kaarten()->list[Kaart]:
    kaarten=[]
    for naam in NAMEN:
        for kleur in KLEUREN:
            kaarten.append(Kaart(kleur, naam))
    if len(kaarten)!=52:
        raise 
    return kaarten
class test_kaartspel(unittest.TestCase):
    def test_constructor(self):
        kaarten=[]
        for naam in NAMEN:
            for kleur in KLEUREN:
                kaarten.append(Kaart(kleur,naam))
        self.assertEqual(len(kaarten),52)

    def test_properties(self):
        kaarten=[]
        for naam in NAMEN:
            for kleur in KLEUREN:
                kaarten.append(Kaart(kleur,naam))
        for kaart in kaarten:
            self.assertEqual(type(kaart.naam),str)
            self.assertEqual(type(kaart.kleur),str)
            self.assertIn(kaart.naam,NAMEN)
            self.assertIn(kaart.kleur,KLEUREN)

class test_speler(unittest.TestCase):
    def test_constructor(self):
        speler = Speler("Mark",200)
    def test_properties(self):
        speler = Speler("Mark",200)
        self.assertTrue(speler.bij)
        self.assertEqual(speler.naam,"Mark")
        self.assertEqual(speler.moneys,200)
    def test_Interop_kaartspel(self):       #interoperability between modules
        speler = Speler("Mark",200)
        kaarten=maak_kaarten()
        kaarten=speler.pak_kaarten(kaarten)
        self.assertEqual(type(speler.inHand),tuple)
        self.assertEqual(len(speler.inHand),2)
        self.assertEqual(len(kaarten),50)
        for kaart in speler.inHand:
            self.assertNotIn(kaart,kaarten)
        kaarten = speler.leg_kaarten_terug(kaarten)
        self.assertEqual(len(kaarten),52)
        self.assertEqual(speler.inHand,())
    # def test_kaarten_terugleggen(self): #interoperability between modules
    #     speler = Speler("Mark",200)
    #     pass
    def test_zet_in(self):
        speler = Speler("Mark",200)
        geld_eerst=speler.geld
        speler.ontvang_pot(20)
        geld_na=speler.geld
        self.assertGreater(geld_na,geld_eerst)
    def test_ontvang_pot(self):
        speler = Speler("Mark",200)
        oud_pot=50
        oud_geld=speler.geld
        nieuw_pot = speler.zet_in(10,oud_pot)
        nieuw_geld=speler.geld
        self.assertGreater(nieuw_pot,oud_pot)
        self.assertGreater(oud_geld,nieuw_geld)


if __name__ == '__main__':
    unittest.main()