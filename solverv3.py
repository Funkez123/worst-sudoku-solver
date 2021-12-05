import numpy as np
import random
import os

board = [  ## Spielfeld
    [3, 1, 6, 4, 0, 8, 0, 2, 5],
    [0, 8, 9, 6, 1, 0, 3, 4, 7],
    [7, 0, 2, 9, 5, 3, 0, 6, 1],
    [2, 6, 8, 0, 9, 1, 4, 0, 3],
    [1, 9, 0, 8, 4, 7, 2, 5, 0],
    [4, 7, 5, 3, 0, 6, 1, 9, 8],
    [0, 2, 4, 1, 6, 5, 7, 3, 9],
    [6, 3, 7, 0, 8, 9, 5, 1, 0],
    [9, 5, 0, 7, 3, 0, 6, 8, 2]
]

board_constants = [  ## Konstanten des Spielfelds
    [0, 6, 0, 5, 0, 8, 7, 0, 3],
    [9, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [5, 0, 8, 0, 0, 3, 0, 0, 9],
    [0, 7, 3, 0, 0, 1, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 1, 0, 0, 0, 0, 3, 2, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 6, 0, 5, 0, 0]
]

w,h = 9,9

i = 0
for i in range(w):
    print(board[i])

#print("##############")

var_zeile = 0
var_spalte = 0
for var_spalte in range(h):
        for var_zeile in range(w):
            if board[var_zeile][var_spalte] != 0:
                board_constants[var_zeile][var_spalte] = 1 #creates a comparision map

#print for checkup

for k in range(w):
    print(board_constants[k])

#print("first step: (zufaellige Zahlen)")

n_error = 1

### random number assigner
def rand_num():
    var_zeile = 0
    var_spalte = 0
    for var_spalte in range(h):
        for var_zeile in range(w):
            if board_constants[var_zeile][var_spalte] != 1:
                board[var_zeile][var_spalte]=random.randint(1,9)

i = 0
for i in range(w):
    print(board[i])

### Error checker ###

print("second step: (error checker)")

x_values_error = 0
error_accuarcy = [200]

def error_checker():
    # zeilen_check
    n_error = 0 # Startfehleranzahl = 0
    for var_zeile in range(w):
        sortierte_zeile = sorted(board[var_zeile])
        #print(sortierte_zeile)
        # duplikat-check
        dup_z = 0
        for dup_z in range(h-1):
            if sortierte_zeile[dup_z] == sortierte_zeile[dup_z+1]:
                n_error = (n_error + 1)

    ## Reihen_check
    for var_reihe in range(h):
        sortierte_zeile = sorted(board[var_reihe])
        #print(sortierte_zeile)
        # duplikat-check
        dup_z = 0
        for dup_z in range(w-1):
            if sortierte_zeile[dup_z] == sortierte_zeile[dup_z+1]:
                n_error = (n_error + 1)

    ### Box_Check
    box_num_reihe = 0
    box_num_spalte = 0
    box_list = [0,0,0,0,0,0,0,0,0]
    for box_num_spalte in range (3):
        for box_num_reihe in range(3):
            #box_num_reihe*3

            box_list[0] = board[box_num_reihe*3][box_num_spalte*3]
            box_list[1] = board[box_num_reihe*3+1][box_num_spalte*3]
            box_list[2] = board[box_num_reihe*3+2][box_num_spalte*3]
            box_list[3] = board[box_num_reihe*3][box_num_spalte*3+1]
            box_list[4] = board[box_num_reihe*3+1][box_num_spalte*3+1]
            box_list[5] = board[box_num_reihe*3+2][box_num_spalte*3+1]
            box_list[6] = board[box_num_reihe*3][box_num_spalte*3+2]
            box_list[7] = board[box_num_reihe*3+1][box_num_spalte*3+2]
            box_list[8] = board[box_num_reihe*3+2][box_num_spalte*3+2]

            box_list_sorted = sorted(box_list)

            #print(box_list_sorted)

            dub_z = 0

            for dup_z in range(h-1):
                if sortierte_zeile[dup_z] == sortierte_zeile[dup_z+1]:
                    n_error = (n_error + 1)

    global error_accuarcy
    global x_values_error
    global update_flag
    if n_error < error_accuarcy[x_values_error]:
        error_accuarcy.append(n_error)
        update_flag = "true"
        #print(error_accuarcy)
        x_values_error = x_values_error + 1


def safe_checker_box(currentx,currenty):
    print("lol")



def clearConsole():  ## cleart den Terminal damit es schicker aussieht
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def consoleprint():
    clearConsole()

    print("##########################################################")
    print("")
    i = 0
    for i in range(w):
        print("             " + str(board[i]) + "                   ")
    print("")
    print("##########################################################")
    print("Error_accuracy:")
    print(error_accuarcy[x_values_error])
    print("##########################################################")
    print("Iterationsnummer : ")
    print(iterationen)
    print("##########################################################")
    print("Fortschritt:" + str(100-error_accuarcy[x_values_error]) + "%")
    print("##########################################################")
    print("Prozess mit CTRL+C beenden")

iterationen = 0

while error_accuarcy != 0:
    iterationen = iterationen + 1
    temp_error_accuarcy = error_accuarcy[x_values_error]
    rand_num()
    error_checker()

    if error_accuarcy[x_values_error] != temp_error_accuarcy:
        consoleprint()

    if iterationen%1000 == 0:   ## aller 1000 Iterationen einfach das Fenster updaten
        consoleprint()

if error_accuarcy == 0:
    print("gelöst in" + str(iterationen))
