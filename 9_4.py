from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

# Czekaj 60 sekund
time.sleep(60)

# Pobierz listę uderzeń w bloki
trafieniaWbloki = mc.events.pollBlockHits()

# Wyświetl na czacie długość listy uderzeń w bloki
dlugoscListyTrafien = len(trafieniaWbloki)
mc.postToChat("Twoj wynik to " + str(dlugoscListyTrafien))
