from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 6
y = 5
z = 28
typBloku = 103
wyzej = 1
mc.setBlock(x, y, z, typBloku)
mc.setBlock(x, y + wyzej, z, typBloku)
