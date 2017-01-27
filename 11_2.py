from mcpi.minecraft import Minecraft
mc = Minecraft.create()

listaZadan = open("ListaZadan.txt", "r")

for wiersz in listaZadan:
    mc.postToChat(wiersz)
