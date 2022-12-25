from collections import OrderedDict
from Game import Game
import pygame as py
import random

py.init()

#constants
WIDTH, HEIGHT = 700, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
pos = (-100, 0)
FPS = 60
clock = py.time.Clock()
endgame = False

#create canvas
screen = py.display.set_mode((WIDTH, HEIGHT)) #creating window
py.display.set_caption("WELCOME TO EMMA'S HANGMAN")

#create letters
font1 = py.font.SysFont('chalkduster', 30)
font2 = py.font.SysFont('chalkduster', 20)

#create underscore image and position
underscore_img = font1.render('_', False, BLACK)
guess_word_positions = [(357, 174), (387, 174), (417, 174), (447, 174), (477, 174), (507, 174), (537, 174), (567, 174), (597, 174), (627, 174), (657, 174)]

def create_letters():
    #ordered dict char -> tuple : {letter: (letter_image, xPos, yPos)}
    letters = OrderedDict()

    a_img = font1.render('A', False, BLACK)
    letters['A'] = (a_img, 140, 420)

    b_img = font1.render('B', False, BLACK)
    letters['B'] = (b_img, 200, 420)

    c_img = font1.render('C', False, BLACK)
    letters['C'] = (c_img, 260, 420)

    d_img = font1.render('D', False, BLACK)
    letters['D'] = (d_img, 320, 420)

    e_img = font1.render('E', False, BLACK)
    letters['E'] = (e_img, 380, 420)

    f_img = font1.render('F', False, BLACK)
    letters['F'] = (f_img, 440, 420)

    g_img = font1.render('G', False, BLACK)
    letters['G'] = (g_img, 500, 420)

    h_img = font1.render('H', False, BLACK)
    letters['H'] = (h_img, 560, 420)

    i_img = font1.render('I', False, BLACK)
    letters['I'] = (i_img, 110, 470)

    j_img = font1.render('J', False, BLACK)
    letters['J'] = (j_img, 170, 470)

    k_img = font1.render('K', False, BLACK)
    letters['K'] = (k_img, 230, 470)

    l_img = font1.render('L', False, BLACK)
    letters['L'] = (l_img, 290, 470)

    m_img = font1.render('M', False, BLACK)
    letters['M'] = (m_img, 350, 470)

    n_img = font1.render('N', False, BLACK)
    letters['N'] = (n_img, 410, 470)

    o_img = font1.render('O', False, BLACK)
    letters['O'] = (o_img, 470, 470)

    p_img = font1.render('P', False, BLACK)
    letters['P'] = (p_img, 530, 470)

    q_img = font1.render('Q', False, BLACK)
    letters['Q'] = (q_img, 140, 520)

    r_img = font1.render('R', False, BLACK)
    letters['R'] = (r_img, 200, 520)

    s_img = font1.render('S', False, BLACK)
    letters['S'] = (s_img, 260, 520)

    t_img = font1.render('T', False, BLACK)
    letters['T'] = (t_img, 320, 520)

    u_img = font1.render('U', False, BLACK)
    letters['U'] = (u_img, 380, 520)

    v_img = font1.render('V', False, BLACK)
    letters['V'] = (v_img, 440, 520)

    w_img = font1.render('W', False, BLACK)
    letters['W'] = (w_img, 500, 520)

    x_img = font1.render('X', False, BLACK)
    letters['X'] = (x_img, 560, 520)

    y_img = font1.render('Y', False, BLACK)
    letters['Y'] = (y_img, 290, 570)

    z_img = font1.render('Z', False, BLACK)
    letters['Z'] = (z_img, 350, 570)

    return letters

def get_words():
    f = open("words.txt")
    list = f.readlines()
    f.close()
    return list

def spot_letter(x, y, o_dict):
    for k, v in o_dict.items():
        lower_x = v[1]
        upper_x = v[1] + 30

        lower_y = v[2]
        upper_y = v[2] + 30

        if lower_x <= x <= upper_x and lower_y <= y <= upper_y:
            print(k)
            return k

    return '-'

def spot_choice(x, y):
    menu_choices = {'NEW GAME': (256, 300, 440, 334),
                    'INSTRUCTIONS': (228, 408, 472, 431),
                    'EXIT': (309, 510, 390, 532)}

    for k,v in menu_choices.items():
        if v[0] <= x <= v[2] and v[1] <= y <= v[3]:
            print(k)
            return k
    return '-'

def spot_restart_or_quit(x,y):
    menu_choices = {'MAIN MENU': (24, 632, 155, 653),
                    'EXIT': (517, 631, 652, 653)}

    for k, v in menu_choices.items():
        if v[0] <= x <= v[2] and v[1] <= y <= v[3]:
            print(k)
            return k
    return '-'

def end_message(game, message):
    screen.fill(WHITE)

    solution_header = font1.render("THE CORRECT WORD WAS... ", False, BLACK)
    screen.blit(solution_header, dest= ((WIDTH / 2 - solution_header.get_width() / 2), 60))

    end_message = font1.render(message, False, BLACK)

    # find middle of screen
    text_width = WIDTH / 2 - end_message.get_width() / 2
    text_height = HEIGHT / 2 - end_message.get_height() / 2

    if message == "GAME OVER!":
        solution = font1.render(game.wordString, False, RED)
        lose_screen = py.image.load("images/drawisland (8).png")
        screen.blit(lose_screen, dest= (0, 200))
    else:
        solution = font1.render(game.wordString, False, GREEN)

    screen.blit(solution, dest=((WIDTH / 2 - solution.get_width() / 2), 150))
    screen.blit(end_message, (text_width, text_height))

    back_to_main = font2.render("MAIN MENU", False, BLACK)
    screen.blit(back_to_main, dest= (25, 630))
    exit_game = font2.render("EXIT GAME", False, BLACK)
    screen.blit(exit_game, dest= (520, 630))


    # py.draw.rect(screen, BLACK, py.Rect(100, 400, 500, 200), 2)
    # py.draw.rect(screen, BLACK, py.Rect(50, 500, 50, 50), 2)

def sketch(game, img, letters):
    screen.fill(WHITE)
    screen.blit(img, dest=pos)  # blit renders the game object onto the surface

    for char, tuple in letters.items():
        screen.blit(tuple[0], (tuple[1], tuple[2]))

    for i, chr in enumerate(game.wordArray):
        if chr != '_':
            chr_img = font1.render(chr, False, BLACK)
            screen.blit(chr_img, dest=guess_word_positions[i])

    for i in range(len(game.wordArray)):
        p = guess_word_positions[i]
        screen.blit(underscore_img, dest=(p[0], p[1] + 5))

    # py.draw.rect(screen, BLACK, py.Rect(25, 630, 100, 50), 2)
    # py.draw.rect(screen, BLACK, py.Rect(570, 630, 100, 50), 2)

def snow_coordinates(snow):
    for i in range(50):
        x = random.randrange(0, 700)
        y = random.randrange(0, 700)
        snow.append([x, y])

def start_game():
    #import endgame
    global endgame

    # load image
    img = py.image.load("images/drawisland (0).png")
    game_status = 0

    letters = create_letters()
    game = Game(get_words(), letters)
    exit = False
    while not exit:
        clock.tick(FPS) #making the while loop run at that FPS

        for event in py.event.get():
            # terminates event when the close button is clicked
            if event.type == py.QUIT:
                exit = True

            if event.type == py.MOUSEBUTTONDOWN:
                mouse_pos = py.mouse.get_pos()
                print(mouse_pos)
                choice = spot_letter(mouse_pos[0], mouse_pos[1], letters)

                #if user clicked a letter
                if choice != '-':
                    del letters[choice]
                    found = game.play(choice)
                    if not found and game_status < 6:
                        game_status += 1


                    print(game.wordString)
                    print(game.letterSet)

                img = py.image.load("images/drawisland (" + str(game_status) + ").png")

                if endgame:
                    print("hi")
                    endgame_choice = spot_restart_or_quit(mouse_pos[0], mouse_pos[1])
                    if endgame_choice == 'MAIN MENU':
                        main_menu()
                        exit = True
                    elif endgame_choice == 'EXIT':
                        exit = True

        sketch(game, img, letters)

        # win condition
        if game.emptyCellCount == 0:
            endgame = True
            end_message(game, "YOU WON!")

        # lose condition
        elif game_status == 6:
            endgame = True
            game.wordArray = ['_' for i in range(10)] #to avoid win screen taking over lose screen in case of random clicks
            end_message(game, "GAME OVER!")

        # pygame.draw.rect(screen, rect_color, py.Rect(100, 400, 500, 200), 2)
        py.display.update()

def main_menu():

    exit = False
    while not exit:
        clock.tick(FPS) #making the while loop run at that FPS
        screen.fill(WHITE)

        snow = []
        snow_coordinates(snow)

        for ice in range(len(snow)):  # in this loop we draw a circle for the coordinate in the snow list
            py.draw.circle(screen, 'sky blue', snow[ice], 3)
            snow[ice][1] += 1  # we are increasing the y coordinate by one as we want the fall effect
            if snow[ice][1] > 700:  # we put a condition when the coordinate y as we are constantly increasing it
                # exceeds the length of screen we assign a complete new coordinate
                snow[ice][1] = random.randrange(-50,-10)  # y is negative as we wanna start from top again and increase y
                snow[ice][0] = random.randrange(0, 700)  # assigning the x coordinate a new value
        clock.tick(5)#giving framerate how fast the snow falls by def it is 0 the larger the framerate the slower the snow fall


        menu_title = font1.render("WELCOME TO EMMA'S HANGMAN", False, BLACK)
        screen.blit(menu_title, dest= ((WIDTH / 2 - menu_title.get_width() / 2), 100))

        play_button = font1.render("NEW GAME", False, BLACK)
        screen.blit(play_button, dest=((WIDTH / 2 - play_button.get_width() / 2), 300))

        instructions_button = font1.render("INSTRUCTIONS", False, BLACK)
        screen.blit(instructions_button, dest=((WIDTH / 2 - instructions_button.get_width() / 2), 400))

        exit_button = font1.render("EXIT", False, BLACK)
        screen.blit(exit_button, dest=((WIDTH / 2 - exit_button.get_width() / 2), 500))

        for event in py.event.get():
            # terminates event when the close button is clicked
            if event.type == py.QUIT:
                exit = True

            if event.type == py.MOUSEBUTTONDOWN:
                mouse_pos = py.mouse.get_pos()
                print(mouse_pos)
                choice = spot_choice(mouse_pos[0], mouse_pos[1])
                if choice != '-':
                    if choice == 'NEW GAME':
                        start_game()
                        exit = True
                    if choice == 'EXIT':
                        exit = True
        py.display.update()

main_menu()
