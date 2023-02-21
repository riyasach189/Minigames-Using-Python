import pygame
import random
import button
import os
pygame.font.init()

def init():
    import pygame
    import random
    import button
    import os
    pygame.font.init()

    USER_WINS = 0
    CPU_WINS = 0
    WIDTH, HEIGHT = 1290, 650
    CARD_WIDTH, CARD_HEIGHT = 150,150
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Elements Unleashed')
    SCORE_FONT = pygame.font.SysFont('arcadeclassic', 40)
    WIN_FONT = pygame.font.SysFont('arcadeclassic', 100)
    run = True
    card_deck = make_deck(CARD_WIDTH, CARD_HEIGHT)
    card_chosen = pygame.image.load(r"button_transparent.png").convert_alpha()


class Card:
    def __init__(self, name, image):
        self.name = name
        self.img = image

def make_deck(CARD_WIDTH,CARD_HEIGHT):
    deck = []
    for _ in range(5):
        card_name = random.choice(['snow','fire','water'])
        card = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Elementsunleashed',card_name+".png")),(CARD_WIDTH,CARD_HEIGHT))
        card_obj = Card(card_name,card)
        deck.append(card_obj)
    return deck

def create_buttons():
    button_img = pygame.image.load(r"button_transparent.png").convert_alpha()
    buttons = list()
    for i in range(5):
        buttons.append(button.Button(150+200*i,485, button_img,1))
    return buttons

def who_won(a,b, SCORE_FONT, WIN, WIDTH, USER_WINS, CPU_WINS):
    if a.name == b.name:
        winner = SCORE_FONT.render("Draw",1,(255,255,255))
        WIN.blit(winner, (WIDTH//2-90,100))
        pygame.display.update()
        pygame.time.delay(1000)
    elif (a.name == "snow" and b.name == "fire") or (a.name == "fire" and b.name == "water") or (a.name == "water" and b.name == "snow"):
        winner = SCORE_FONT.render("You won this round",1,(255,255,255))
        WIN.blit(winner, (WIDTH//2-170,100))
        pygame.display.update()
        pygame.time.delay(1000)
        USER_WINS += 1
    else:
        winner = SCORE_FONT.render("CPU won this round",1,(255,255,255))
        WIN.blit(winner, (WIDTH//2-170,100))
        pygame.display.update()
        pygame.time.delay(1000)
        CPU_WINS += 1
    return(USER_WINS,CPU_WINS)
run = True
def elementsunleashed(): 
    init()   
    USER_WINS = 0
    CPU_WINS = 0
    WIDTH, HEIGHT = 1290, 650
    CARD_WIDTH, CARD_HEIGHT = 150,150
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Elements Unleashed')
    SCORE_FONT = pygame.font.SysFont('arcadeclassic', 40)
    WIN_FONT = pygame.font.SysFont('arcadeclassic', 100)
    run = True
    card_deck = make_deck(CARD_WIDTH,CARD_HEIGHT)
    card_chosen = pygame.image.load(r"button_transparent.png").convert_alpha()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(1290,650))
        WIN.blit(bg,(0,0))
        for i in range(5):
            try:
                WIN.blit(card_deck[i].img,(150+200*i,485))
            except:
                continue
        buttons = create_buttons()

        for i in range(5):
            if buttons[i].draw(WIN):
                card_chosen = card_deck[i].img
                user_card = card_deck[i]
                card_deck[i].img = pygame.image.load(r"button_transparent.png").convert_alpha()
                card_deck[i].img = 0
                card_chosen = pygame.transform.scale(card_chosen,(200,200))
                WIN.blit(card_chosen,(250,100))
                pygame.display.update()
                pygame.time.delay(500)
                card_name = random.choice(['snow','fire','water'])
                card = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Elementsunleashed',card_name+".png")),(200,200))
                cpu_card = Card(card_name,card)
                WIN.blit(cpu_card.img, (750,100))
                pygame.display.update()
                USER_WINS, CPU_WINS = who_won(cpu_card,user_card, SCORE_FONT, WIN, WIDTH, USER_WINS, CPU_WINS)
                pygame.display.update()
                if USER_WINS == 3:
                    winner = WIN_FONT.render("YOU WON!",1,(255,255,255))
                    WIN.blit(winner, (WIDTH//2-170,300))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    CPU_WINS = 0
                    USER_WINS = 0
                elif CPU_WINS == 3:
                    winner = WIN_FONT.render("YOU LOST",1,(255,255,255))
                    WIN.blit(winner, (WIDTH//2-170,300))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    CPU_WINS = 0
                    USER_WINS = 0
                break
        for i in range(5):
            if card_deck[i].img == 0:
                card = pygame.transform.scale(pygame.image.load(os.path.join('Assets_Elementsunleashed',card_name+".png")),(CARD_WIDTH,CARD_HEIGHT))
                card_obj = Card(card_name,card)
                card_deck[i] = card_obj
        user_score = SCORE_FONT.render(f"Your wins: {USER_WINS}",1,(255,255,255))
        WIN.blit(user_score, (15,15))
        cpu_score = SCORE_FONT.render(f"CPU wins: {CPU_WINS}",1,(255,255,255))
        WIN.blit(cpu_score, (WIDTH-cpu_score.get_width()-15,15))
        pygame.display.update()
