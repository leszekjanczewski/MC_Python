import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz1 = mc.player.getTilePos()
x1 = poz1.x
y1 = poz1.y
z1 = poz1.z

time.sleep(10)

poz2 = mc.player.getTilePos()
x2 = poz2.x
y2 = poz2.y
z2 = poz2.z

# Oblicz różnicę między pozycją początkową a końcową
xOdleglosc = x2 - x1
yOdleglosc = y2 - y1
zOdleglosc = z2 - z1

# Wyślij wyniki obliczeń na czat
mc.postToChat("Gracz poruszyl sie o x: " + str(xOdleglosc) + ", y: "
    + str(yOdleglosc) + ", and z: " + str(zOdleglosc))
