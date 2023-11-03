class Kaart:
    def __init__(self, kleur, naam):
        self.kleur = kleur
        self.naam = naam

    def show(self):
        print(f"{self.kleur} {self.naam}")
    def get(self):
        return (self.kleur, self.naam)

namen = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H", "A")
kleuren = ("Harten", "Klaveren", "Ruiten", "Schoppen")
kaarten = []
for naam in namen:
    for kleur in kleuren:
        kaarten.append(kaartspel.Kaart(kleur, naam))
KARTEN = tuple(kaarten)
dek = list(KARTEN)
import random
import pygame

pygame.font.init()
GLOBAL_FONT = pygame.font.SysFont("calibri", 18)
WIDTH, HEIGTH = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("HEEEEEEEEEEEEEEELP")
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
FPS = 60
Spelers = {}


class Speler:
    def __init__(self, naam, starterskapitaal, prioriteit):
        self.hand = []
        self.naam = naam
        self.geld = starterskapitaal
        self.prioriteit = prioriteit
        self.bij=True

    def inHand(self):  # Returns tuple of cards in hand
        return tuple(self.hand)

    def pak_kaarten(self):  # pakt 2 random kaarten en haalt die uit dek
        self.kaart1 = random.choice(
            dek
        )  # raise error als dek te weinig kaarten heeft???
        dek.remove(self.kaart1)
        self.kaart2 = random.choice(dek)
        dek.remove(self.kaart2)
        self.hand.append(self.kaart1)
        self.hand.append(self.kaart2)

    def leg_kaarten_terug(self):
        self.kaart1 = self.hand[0]
        self.kaart2 = self.hand[1]
        self.hand.clear()
        dek.append(self.kaart1)
        dek.append(self.kaart2)

    def ontvang_pot(self,pot):
        self.geld+=pot
    def zet_in(self,inzet,pot): #raise error als te weinig geld?
        self.geld-=inzet
        return pot+inzet
    def moneys(self):
        return self.geld

def main():
    print("Starting...")
    clock = pygame.time.Clock()
    aantal_spelers = startscreen(clock)
    run = True
    setup(aantal_spelers, clock)
    print("Ga de while loop van main in")
    # starting_player=0
    deler=0

    while run:
        print("start while loop main")
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("de game is klaar")
                run = False
        potje(Spelers,deler,aantal_spelers)
        # for speler in Spelers:
        #     if Spelers[speler].prioriteit==current:
        #         print(f"Speler {speler} is aan de beurt")
        #         WIN.fill(BLACK)
        #         tekst=GLOBAL_FONT.render('Speler met de naam {speler.naam} is aan de beurt')
        deler+=1
        if deler>aantal_spelers-1:
            deler=0

    print("Game over")
    pygame.quit()


def draw():
    pass


PADDING = 10


def startscreen(clock):
    WIN.fill(BLACK)
    tekst1 = GLOBAL_FONT.render("Welkom bij poker", 1, WHITE)
    tekst2 = GLOBAL_FONT.render("Typ het aantal spelers", 1, WHITE)
    WIN.blit(tekst1, (PADDING, PADDING))
    WIN.blit(tekst2, (PADDING, PADDING + tekst1.get_height()))
    pygame.display.update()
    # aantal_spelers=input(" ")
    input_given = False
    print("waiting for input")
    while not input_given:
        clock.tick(FPS)
        print("in while loop code 1")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("de game is klaar")
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_2] == True:
            print("valid value pressed")
            aantal_spelers = 2
            input_given = True
        if keys_pressed[pygame.K_3] == True:
            print("valid value pressed")
            aantal_spelers = 3
            input_given = True
        if keys_pressed[pygame.K_4] == True:
            print("valid value pressed")
            aantal_spelers = 4
            input_given = True
        if keys_pressed[pygame.K_5] == True:
            print("valid value pressed")
            aantal_spelers = 5
            input_given = True
        if keys_pressed[pygame.K_6] == True:
            print("valid value pressed")
            aantal_spelers = 6
            input_given = True
        if keys_pressed[pygame.K_7] == True:
            print("valid value pressed")
            aantal_spelers = 7
            input_given = True
        if keys_pressed[pygame.K_8] == True:
            print("valid value pressed")
            aantal_spelers = 8
            input_given = True
        if keys_pressed[pygame.K_9] == True:
            print("valid value pressed")
            aantal_spelers = 9
            input_given = True
    print(f"Het aantal spelers is {aantal_spelers}")
    return aantal_spelers
def increment(i,max):
    return (i+1)%max

def setup(aantal_spelers, clock):
    for i in range(aantal_spelers):
        key = "speler " + str(i + 1)
        value = Speler("Spler " + str(i + 1), 200, i)
        Spelers.update({key: value})
    print(Spelers)
    WIN.fill(BLACK)
    tekst1 = GLOBAL_FONT.render("De volgende spelers doen mee: ", 1, WHITE)
    WIN.blit(tekst1, (PADDING, PADDING))
    i = 0
    for naam in Spelers:
        i += 1
        tekst = GLOBAL_FONT.render(naam + " " + Spelers[naam].naam, 1, WHITE)
        WIN.blit(tekst, (PADDING, PADDING + 20 * i))
    tekst2 = GLOBAL_FONT.render("Druk op spatie om te beginnen", 1, WHITE)
    WIN.blit(tekst2, (PADDING + 400, PADDING))
    pygame.display.update()

    spacebar_pressed = False
    while not spacebar_pressed:
        clock.tick(FPS)
        print("in while loop code 2")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("de game is klaar")
                pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE] == True:
            spacebar_pressed = True
    state=1

def potje(Spelers,deler,aantal_spelers):
    pot=0 #keep track of pot
    potje_bezig=True
    aan_de_beurt=increment(deler,aantal_spelers)
    small=aan_de_beurt
    pot=Spelers['Speler '+str(small)].zet_in(1,pot)
    aan_de_beurt=increment(deler,aantal_spelers)
    big=aan_de_beurt
    pot=Spelers['Speler '+str(big)].zet_in(2,pot)
    while potje_bezig:
        aan_de_beurt=increment(deler,aantal_spelers) #Hier ben ik gebleven



main()
