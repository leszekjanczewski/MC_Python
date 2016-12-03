from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pozycja = mc.player.getTilePos()
x = pozycja.x
y = pozycja.y
z = pozycja.z

y = y + 10

mc.player.setTilePos(x, y, z)
