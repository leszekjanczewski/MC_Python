from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import pickle


def sortujPary(wart1, wart2):
    if wart1 > wart2:
        return wart2, wart1
    else:
        return wart1, wart2


def kopiujStrukture(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortujPary(x1, x2)
    y1, y2 = sortujPary(y1, y2)
    z1, z2 = sortujPary(z1, z2)

    szer = x2 - x1
    wys = y2 - y1
    dlug = z2 - z1

    struktura = []

    print("Prosze czekac...")

    # Kopiuj strukture
    for wiersz in range(wys):
        struktura.append([])
        for kolumna in range(szer):
            struktura[wiersz].append([])
            for gleb in range(dlug):
                blok = mc.getBlockWithData(x1 + kolumna, y1 + wiersz, z1 + gleb)
                struktura[wiersz][kolumna].append(blok)

    return struktura

input("Przejdz do pierwszego naroznika i nacisnij enter w tym oknie")
poz1 = mc.player.getTilePos()

# Pobierz pozycję pierwszego narożnika
x1 = poz1.x
y1 = poz1.y
z1 = poz1.z

input("Przejdz do drugiego naroznika i nacisnij ENTER w tym oknie")
poz2 = mc.player.getTilePos()

# Pobierz pozycję drugiego narożnika
x2 = poz2.x
y2 = poz2.y
z2 = poz2.z

struktura = kopiujStrukture(x1, y1, z1, x2, y2, z2)

# Zapisz strukturę w pliku
plikPickle = open("plikPickle", "wb")
pickle.dump(struktura, plikPickle)
