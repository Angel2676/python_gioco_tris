def display_lavagna(lavagna):
    griglia_vuota="""
___________________
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
"""
    for i in range(1,10):
        if (lavagna[i] == 'O' or lavagna[i] == 'X'):
            griglia_vuota = griglia_vuota.replace(str(i), lavagna[i])
    print(griglia_vuota)

def area_gioco(lavagna, segno, posizione):
    lavagna[posizione] = segno
    return lavagna

def lavagna_piena(lavagna):
    return len([x for x in lavagna if x == '#']) == 1

def inserimento_giocatore():
    giocatore1 = input("scegli  'X' o  'O' ")
    while True:
        if (giocatore1 == 'X' or giocatore1 == 'x'):
            giocatore1 ='X'
            giocatore2='O'
            print("Hai scelto " + giocatore1 + ". \nGiocatore 2 sarà  " + giocatore2)
            return giocatore1,giocatore2
        elif giocatore1 == 'O':
            giocatore2='X'
            print("Hai scelto " + giocatore1 + ". \nGiocatore 2 sarà  " + giocatore2)
            return giocatore1,giocatore2
        else:
            giocatore_uno = input("scegli  'X' o  'O' ")

def rigioca():
    giocancora = input("Vuoi giocare ancora (s/n)  ? ")
    if (giocancora == 's' or giocancora == 'S'):
        return True
    if (giocancora == 'n' or giocancora == 'N'):
        return False

def controllo_spazi(lavagna, posizione):
    return lavagna[posizione] == '#'

def controllo_vincita(lavagna, segno):
    if lavagna[1] == lavagna[2] == lavagna[3] == segno:
        return True
    if lavagna[4] == lavagna[5] == lavagna[6] == segno:
        return True
    if lavagna[7] == lavagna[8] == lavagna[9] == segno:
        return True
    if lavagna[1] == lavagna[4] == lavagna[7] == segno:
        return True
    if lavagna[2] == lavagna[5] == lavagna[8] == segno:
        return True
    if lavagna[3] == lavagna[6] == lavagna[9] == segno:
        return True
    if lavagna[1] == lavagna[5] == lavagna[9] == segno:
        return True
    if lavagna[3] == lavagna[5] == lavagna[7] == segno:
        return True
    return False

def giocatore_scelta(lavagna):
    scelta = input("Seleziona uno spazio da 1 a 9 : ")
    while not controllo_spazi(lavagna, int(scelta)):
        scelta = input("Spazio non vuoto, seleziona uno spazio tra 1 e 9 : ")
    return scelta

if __name__ == "__main__":
    print('Benvenuto in Tris')
    i = 1
    giocatori=inserimento_giocatore()
    lavagna = ['#'] * 10
    while True:
        avvia_gioco=lavagna_piena(lavagna)
        while not avvia_gioco:
            posizione = giocatore_scelta(lavagna)
            if i % 2 == 0:
                segno = giocatori[1]
            else:
                segno = giocatori[0]
            area_gioco(lavagna, segno, int(posizione))
            display_lavagna(lavagna)
            i += 1
            if controllo_vincita(lavagna, segno):
                print("Hai vinto")
                break
            avvia_gioco=lavagna_piena(lavagna)
        if not rigioca():
            break
        else:
            i = 1
            giocatori=inserimento_giocatore()
            lavagna = ['#'] * 10