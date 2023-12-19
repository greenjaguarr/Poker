import random
import pygame
from kaartspel import Kaart
from speler import Speler
import sys
#Mark is de goat



namen = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "V", "H", "A")
kleuren = ("Harten", "Klaveren", "Ruiten", "Schoppen")
kaarten = []
for naam in namen:
    for kleur in kleuren:
        kaarten.append(Kaart(kleur, naam))
KARTEN = tuple(kaarten)
dek = list(KARTEN)


pygame.init()
pygame.font.init()
GLOBAL_FONT = pygame.font.SysFont("calibri", 18)
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HEEEEEEEEEEEEEEELP")
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
FPS = 60
Spelers = {}




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

def draw_startscreen()->None:
    '''This function draws the start screen, obviously.
    side effects: alters the display
    :return: None'''
    WIN.fill(BLACK)
    tekst1 = GLOBAL_FONT.render("Welkom bij poker", 1, WHITE)
    tekst2 = GLOBAL_FONT.render("Typ het aantal spelers", 1, WHITE)
    WIN.blit(tekst1, (PADDING, PADDING))
    WIN.blit(tekst2, (PADDING, PADDING + tekst1.get_height()))
    pygame.display.flip()


def startscreen(clock)->int:
    while True:
        draw_startscreen()
        clock.tick(FPS)
        print("in while loop code 1")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("de game is klaar")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_2] == True:
                    return 2
                if keys_pressed[pygame.K_3] == True:
                    return 3
                if keys_pressed[pygame.K_4] == True:
                    return 4
                if keys_pressed[pygame.K_5] == True:
                    return 5
                if keys_pressed[pygame.K_6] == True:
                    return 6
                if keys_pressed[pygame.K_7] == True:
                    return 7
                if keys_pressed[pygame.K_8] == True:
                    return 8
                if keys_pressed[pygame.K_9] == True:
                    return 9
            else:
                #The player entered an invalid key. Let's just not react
                pass

def increment(i,max):
    return (i+1)%max

def setup(aantal_spelers:int, clock):
    for i in range(aantal_spelers):
        key = "speler " + str(i + 1)
        value = Speler("Spler " + str(i + 1), 200)
        Spelers.update({key: value})
    #print(Spelers)
    while True:
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
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                keys_pressed=pygame.key.get_pressed()
                if keys_pressed[pygame.K_SPACE]==True:
                    break #continue #or break??

def potje(Spelers,deler,aantal_spelers):
    pot=0 #keep track of pot
    potje_bezig=True
    for speler in Spelers:         #Deel kaarten uit
        Spelers[speler].pak_kaarten()
    aan_de_beurt=increment(deler,aantal_spelers)
    small=aan_de_beurt
    pot=Spelers['Speler '+str(small+1)].zet_in(1,pot)
    aan_de_beurt=increment(deler,aantal_spelers)
    big=aan_de_beurt
    pot=Spelers['Speler '+str(big+1)].zet_in(2,pot)
    
    midden=[]
    kaart1=random.choice(dek)  # raise error als dek te weinig kaarten heeft???
    dek.remove(kaart1)
    kaart2=random.choice(dek)  # raise error als dek te weinig kaarten heeft???
    dek.remove(kaart2)
    kaart3=random.choice(dek)  # raise error als dek te weinig kaarten heeft???
    dek.remove(kaart3)
    midden.append(kaart1)
    midden.append(kaart2)
    midden.append(kaart3)
    
    while potje_bezig:
        aan_de_beurt=increment(deler,aantal_spelers)
        speler = Spelers['Speler '+str(aan_de_beurt)] #Get the Speler object die nu aan de beurt is
        for kaart in speler.hand: #extraheer welke kaarten de speler in zn handen heeft in losse variables
            kaart1 = kaart.get() # geeft tuple in de vorm (kleur, naam)
            kaart2 = kaart.get()
        #[extract functie hier om de kaarten in het midden, de kaarten in de hand, de pot, het geld van de speler en welke andere spelers nog mee doen te laten zien. 
        #Pak user input om te kiezen voor raise,check of pas. Check of het een valide input is.]


if __name__ == '__main__':
    main()