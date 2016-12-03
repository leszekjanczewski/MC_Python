from mcpi.minecraft import Minecraft
mc = Minecraft.create()

poz = mc.player.getTilePos()
x = poz.x
y = poz.y
z = poz.z

try:
    typBloku = int(input("Podaj typ bloku: "))
    mc.setBlock(x, y, z, typBloku)
except:
    mc.postToChat("To nie jest liczba! Nastepnym razem podaj liczbe.")



