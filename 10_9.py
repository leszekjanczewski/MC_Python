from mcpi.minecraft import Minecraft
mc = Minecraft.create()


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

    # Kopiuj strukturę
    for wiersz in range(wys):
        struktura.append([])
        for kolumna in range(szer):
            struktura[wiersz].append([])
            for gleb in range(dlug):
                blok = mc.getBlock(x1 + kolumna, y1 + wiersz, z1 + gleb)
                struktura[wiersz][kolumna].append(blok)

    return struktura


def budujStrukture(x, y, z, struktura):
    xPocz = x
    yPocz = y
    for wiersz in struktura:
        for kolumna in wiersz:
            for blok in kolumna:
                mc.setBlock(x, y, z, blok)
                z += 1
            x += 1
            z = yPocz
        y += 1
        x = xPocz


# Pobierz pozycję pierwszego narożnika
input("Przejdz do pierwszego naroznika i nacisnij ENTER w tym oknie")
poz = mc.player.getTilePos()
x1, y1, z1 = poz.x, poz.y, poz.z

# Pobierz pozycję drugiego narożnika
input("Przejdz do drugiego naroznika i nacisnij ENTER w tym oknie")
poz = mc.player.getTilePos()
x2, y2, z2 = poz.x, poz.y, poz.z

# Skopiuj budowlę
struktura = kopiujStrukture(x1, y1, z1, x2, y2, z2)

# Ustaw pozycję kopii
input("Przejdz do miejsca, gdzie chcesz tworzyc strukture i nacisnij ENTER w tym oknie")
poz = mc.player.getTilePos()
x, y, z = poz.x, poz.y, poz.z
budujStrukture(x, y, z, struktura)
