from mcpi.minecraft import Minecraft
mc = Minecraft.create()

miejsca = {"Dom": (10, 11, 12),
          "Wieza": (20, -2, 3),
          "Magazyn": (6, 2, 1)}

wybor = ""
while wybor != "exit":
    wybor = input("Podaj miejsce ('exit' aby przerwac): ")
    if wybor in miejsca:
        lokalizacja = miejsca[wybor]
        x, y, z = lokalizacja[0], lokalizacja[1], lokalizacja[2]
        mc.player.setTilePos(x, y, z)
