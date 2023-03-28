import os
import readchar
from random import randint
# CONSTANTS LIVES
INITIAL_PIKACHU_LIFE = 100
INITIAL_CHARIZARD_LIFE = 100
INITIAL_LUCARIO_LIFE = 100
INITIAL_GRENINJA_LIFE = 100
INITIAL_SNORLAX_LIFE = 100
# ATTACKS
ANILLO_IGNEO = 20
BALON_IGNEO = 25
ASALTO_ESTELAR = 25
CONTRATAQUE = 15
CASCADDA = 10
CALAMIDAD = 20
CORPULENCIA = 2
DEMOLICION = 10
ELECTORMENTA = 10
GIGADESCARGA = 15
GIGAVOLTIO_DESTRUCTOR = 30

POS_X = 0
POS_Y = 1

# VARIABLES
obstacle_definition = """\
XXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXX          XXXXXXXXX
XXXXXXXX          XXXXXXXXX
X                       XXX
X                       XXX
X       XXXXXXXXXXXXXXXXXXX
X       XXXXXXXXXXXXXXXXXXX
X       XXXXXXXXXXXXXXXXXXX
X                       XXX
X                       XXX
X                       XXX
X       XXXXXXXXXXXXXXXXXXX
X       XXXXXXXXXXXXXXXXXXX
X       XXXXXXXXXXXXXXXXXXX
X                        XX
X                        XX
X                        XX
XXXXXXXXXXXXXXXXXX       XX
XXXXXXXXXXXXXXXXXX       XX
XXXXXXXXXXXXXXXXXX       XX
XXXXXXXXXXXXXXXXXXXXXXXXXXX\
"""
my_position = [15, 2]
map_enemies = []
end_game = False
died = False

# POKEMON LIVES
pikachu_life = INITIAL_PIKACHU_LIFE
charizard_life = INITIAL_CHARIZARD_LIFE
lucario_life = INITIAL_LUCARIO_LIFE
greninja_life = INITIAL_GRENINJA_LIFE
snorlax_life = INITIAL_SNORLAX_LIFE

# GENERATING MAP SIZE
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# GENERATING ENEMIES
enemie_1 = [22, 4]
enemie_2 = [22, 10]
enemie_3 = [4, 16]
enemie_4 = [22, 19]

map_enemies.append(enemie_1)
map_enemies.append(enemie_2)
map_enemies.append(enemie_3)
map_enemies.append(enemie_4)

while not end_game:

    # DRAWING THE MAP
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("[", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None

            for enemie in map_enemies:
                if enemie[POS_X] == coordinate_x and enemie[POS_Y] == coordinate_y:
                    char_to_draw = " O"

            if obstacle_definition[coordinate_y][coordinate_x] == "X":
                char_to_draw = "XX"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                # POKEMON COMBATS
                # FIRST COMBAT
                if my_position == enemie_1:
                    # FIRST POKÉMON BATTLE
                    while pikachu_life > 0 and charizard_life > 0:
                        # GENERATING LIFE'S BARS
                        os.system("cls")
                        life_bar_pikachu = int(pikachu_life * 10 / INITIAL_PIKACHU_LIFE)
                        life_bar_charizard = int(charizard_life * 10 / INITIAL_CHARIZARD_LIFE)
                        print("\n\nPikachu: [{}{}]".format("❚" * life_bar_pikachu, " " * (10 - life_bar_pikachu)))
                        print("Charizard: [{}{}]\n\n".format("❚" * life_bar_charizard,
                                                             " " * (10 - life_bar_charizard)))

                        # CHARIZARD'S TURN
                        print("El el turno de Charizard\n")
                        ataque_charizard = randint(1, 2)

                        if ataque_charizard == 1:
                            print("Charizard ataca con Anillo igneo.\n")
                            pikachu_life -= ANILLO_IGNEO
                        elif ataque_charizard == 2:
                            print("Charizard ataca con Balon igneo.\n")
                            pikachu_life -= BALON_IGNEO

                        # DELIMITATING PIKACHU'S LIFE
                        if pikachu_life < 0:
                            pikachu_life = 0

                        input("Enter para continuar...")

                        # PIKACHU TURN
                        print("\nEs el turno de Pikachu\n")
                        ataque_pikachu = input("Con que quieres atacar:\n"
                                               "[E]lectormenta\n"
                                               "[G]igadescarga\n"
                                               "Gigavoltio [D]estructor\n")

                        if ataque_pikachu == "E":
                            print("Pikachu ataca con Electormenta.\n")
                            charizard_life -= ELECTORMENTA
                        elif ataque_pikachu == "G":
                            print("Pikachu ataca con Gigadescarga.\n")
                            charizard_life -= GIGADESCARGA
                        elif ataque_pikachu == "D":
                            print("Pikachu ataca con Gigavoltio Destructor.\n")
                            charizard_life -= GIGAVOLTIO_DESTRUCTOR
                        else:
                            print("Pikachu no ataca.\n")

                        # DELIMITATING CHARIZARD'S LIFE
                        if charizard_life < 0:
                            charizard_life = 0
                        # CLEARING THE DISPLAY
                        os.system("cls")
                    if charizard_life < pikachu_life:
                        pikachu_life = INITIAL_PIKACHU_LIFE
                        map_enemies.remove(enemie_1)
                        enemie_1 = None
                    else:
                        end_game = True
                # SECOND COMBAT
                elif my_position == enemie_2:
                    # FIRST POKÉMON BATTLE
                    while pikachu_life > 0 and lucario_life > 0:
                        # GENERATING LIFE'S BARS
                        os.system("cls")
                        life_bar_pikachu = int(pikachu_life * 10 / INITIAL_PIKACHU_LIFE)
                        life_bar_lucario = int(lucario_life * 10 / INITIAL_LUCARIO_LIFE)
                        print("Pikachu: [{}{}]".format("❚" * life_bar_pikachu, " " * (10 - life_bar_pikachu)))
                        print("Lucario: [{}{}]\n\n".format("❚" * life_bar_lucario,
                                                           " " * (10 - life_bar_lucario)))

                        # LUCARIO'S TURN
                        print("El el turno de Lucario\n")
                        ataque_lucario = randint(1, 2)

                        if ataque_lucario == 1:
                            print("Lucario ataca con Asalto Estelar.\n")
                            pikachu_life -= ASALTO_ESTELAR
                        elif ataque_lucario == 2:
                            print("Lucario ataca con Contrataque.\n")
                            pikachu_life -= CONTRATAQUE

                        # DELIMITATING PIKACHU'S LIFE
                        if pikachu_life < 0:
                            pikachu_life = 0

                        input("Enter para continuar...")

                        # PIKACHU TURN
                        print("\nEs el turno de Pikachu\n")
                        ataque_pikachu = input("Con que quieres atacar:\n"
                                               "[E]lectormenta\n"
                                               "[G]igadescarga\n"
                                               "Gigavoltio [D]estructor\n")

                        if ataque_pikachu == "E":
                            print("Pikachu ataca con Electormenta.\n")
                            lucario_life -= ELECTORMENTA
                        elif ataque_pikachu == "G":
                            print("Pikachu ataca con Gigadescarga.\n")
                            lucario_life -= GIGADESCARGA
                        elif ataque_pikachu == "D":
                            print("Pikachu ataca con Gigavoltio Destructor.\n")
                            lucario_life -= GIGAVOLTIO_DESTRUCTOR
                        else:
                            print("Pikachu no ataca.\n")

                        # DELIMITATING CHARIZARD'S LIFE
                        if lucario_life < 0:
                            lucario_life = 0
                        # CLEARING THE DISPLAY
                        os.system("cls")
                    if lucario_life < pikachu_life:
                        pikachu_life = INITIAL_PIKACHU_LIFE
                        map_enemies.remove(enemie_2)
                        enemie_2 = None
                    else:
                        end_game = True
                # THIRD COMBAT
                elif my_position == enemie_3:
                    while pikachu_life > 0 and greninja_life > 0:
                        # GENERATING LIFE'S BARS
                        os.system("cls")
                        life_bar_pikachu = int(pikachu_life * 10 / INITIAL_PIKACHU_LIFE)
                        life_bar_greninja = int(greninja_life * 10 / INITIAL_GRENINJA_LIFE)
                        print("Pikachu: [{}{}]".format("❚" * life_bar_pikachu, " " * (10 - life_bar_pikachu)))
                        print("Greninja: [{}{}]\n\n".format("❚" * life_bar_greninja,
                                                            " " * (10 - life_bar_greninja)))

                        # GRENINJA'S TURN
                        print("El el turno de Greninja\n")
                        ataque_greninja = randint(1, 2)

                        if ataque_greninja == 1:
                            print("Grenija ataca con Cascada.\n")
                            pikachu_life -= CASCADDA
                        elif ataque_greninja == 2:
                            print("Greninja ataca con Calamidad\n")
                            pikachu_life -= CALAMIDAD

                        # DELIMITATING PIKACHU'S LIFE
                        if pikachu_life < 0:
                            pikachu_life = 0

                        input("Enter para continuar...")

                        # PIKACHU TURN
                        print("\nEs el turno de Pikachu\n")
                        ataque_pikachu = input("Con que quieres atacar:\n"
                                               "[E]lectormenta\n"
                                               "[G]igadescarga\n"
                                               "Gigavoltio [D]estructor\n")

                        if ataque_pikachu == "E":
                            print("Pikachu ataca con Electormenta.\n")
                            greninja_life -= ELECTORMENTA
                        elif ataque_pikachu == "G":
                            print("Pikachu ataca con Gigadescarga.\n")
                            greninja_life -= GIGADESCARGA
                        elif ataque_pikachu == "D":
                            print("Pikachu ataca con Gigavoltio Destructor.\n")
                            greninja_life -= GIGAVOLTIO_DESTRUCTOR
                        else:
                            print("Pikachu no ataca.\n")

                        # DELIMITATING CHARIZARD'S LIFE
                        if greninja_life < 0:
                            greninja_life = 0
                        # CLEARING THE DISPLAY
                        os.system("cls")
                    if greninja_life < pikachu_life:
                        pikachu_life = INITIAL_PIKACHU_LIFE
                        map_enemies.remove(enemie_3)
                        enemie_3 = None
                    else:
                        end_game = True
                # FOURTH COMBAT
                elif my_position == enemie_4:
                    while pikachu_life > 0 and snorlax_life > 0:
                        # GENERATING LIFE'S BARS
                        os.system("cls")
                        life_bar_pikachu = int(pikachu_life * 10 / INITIAL_PIKACHU_LIFE)
                        life_bar_snorlax = int(snorlax_life * 10 / INITIAL_GRENINJA_LIFE)
                        print("Pikachu: [{}{}]".format("❚" * life_bar_pikachu, " " * (10 - life_bar_pikachu)))
                        print("Snorlax: [{}{}]\n\n".format("❚" * life_bar_snorlax,
                                                           " " * (10 - life_bar_snorlax)))

                        # SNORLAX'S TURN
                        print("El el turno de Snorlax\n")
                        ataque_snorlax = randint(1, 2)

                        if ataque_snorlax == 1:
                            print("Snorlax ataca con Corpulencia.\n")
                            pikachu_life -= CORPULENCIA
                        elif ataque_snorlax == 2:
                            print("Snorlax ataca con Demolicion.\n")
                            pikachu_life -= DEMOLICION

                        # DELIMITATING PIKACHU'S LIFE
                        if pikachu_life < 0:
                            pikachu_life = 0

                        input("Enter para continuar...")

                        # PIKACHU TURN
                        print("\nEs el turno de Pikachu\n")
                        ataque_pikachu = input("Con que quieres atacar:\n"
                                               "[E]lectormenta\n"
                                               "[G]igadescarga\n"
                                               "Gigavoltio [D]estructor\n")

                        if ataque_pikachu == "E":
                            print("Pikachu ataca con Electormenta.\n")
                            snorlax_life -= ELECTORMENTA
                        elif ataque_pikachu == "G":
                            print("Pikachu ataca con Gigadescarga.\n")
                            snorlax_life -= GIGADESCARGA
                        elif ataque_pikachu == "D":
                            print("Pikachu ataca con Gigavoltio Destructor.\n")
                            snorlax_life -= GIGAVOLTIO_DESTRUCTOR
                        else:
                            print("Pikachu no ataca.\n")

                        # DELIMITATING CHARIZARD'S LIFE
                        if snorlax_life < 0:
                            snorlax_life = 0
                        # CLEARING THE DISPLAY
                        os.system("cls")
                    if snorlax_life < pikachu_life:
                        pikachu_life = INITIAL_PIKACHU_LIFE
                        map_enemies.remove(enemie_4)
                        enemie_4 = None
                    else:
                        end_game = True

                else:
                    pass

            print("{}".format(char_to_draw), end="")
        print("]")

    print("+" + "-" * MAP_WIDTH * 2 + "+")
    print(map_enemies)
    # INTERACTIVE MOVEMENT

    print("Utiliza [WASD] para moverte en el mapa o [Q] para salir.")
    direction = readchar.readchar()

    new_position = None

    if direction == "W" or direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "S" or direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "A" or direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "D" or direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "Q" or direction == "q":
        break

    # GENERATING THE WALLS
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "X":
            my_position = new_position

    # ENDING THE COMBATS

    if pikachu_life == 0 or len(map_enemies) == 0:
        end_game = True



    os.system("cls")

if len(map_enemies) == 0:
    message = "Felicidades has vencido a todos los entrenadores pokemon, eres el mejor !"
    print("\n" + message + "\n" + len(message) * "-")

elif end_game:
    end_game_message = "Lastima, de verdad pense que ibas a ser un verdadeo entrenador pokemon."
    print("\n" + end_game_message + "\n" + len(end_game_message) * "-")