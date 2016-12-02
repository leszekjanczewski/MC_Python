from mcpi.minecraft import Minecraft
import math
import time
import random
mc = Minecraft.create()

celX = random.randint(-127, 127)
celZ = random.randint(-127, 127)
celY = mc.getHeight(celX, celZ)

print(celX, celY, celZ)

blok = 57
mc.setBlock(celX, celY, celZ, blok)
mc.postToChat("Blok ustawiony")

while True:
    poz = mc.player.getPos()
    odleglosc = math.sqrt((poz.x - celX) ** 2 + (poz.z - celZ) ** 2)

    if odleglosc == 0:
        break

    if odleglosc > 100:
        mc.postToChat("Mroz")
    elif odleglosc > 50:
        mc.postToChat("Zimno")
    elif odleglosc > 25:
        mc.postToChat("Cieplo")
    elif odleglosc > 12:
        mc.postToChat("Goraco")
    elif odleglosc > 6:
        mc.postToChat("Parzy!")
    elif odleglosc == 0:
        mc.postToChat("Znalezione")
