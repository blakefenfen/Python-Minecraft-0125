#1-4

#install
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x = 200
y = 200
z = 100

mc.player.setTilePos(x,y,z)
time.sleep(2)

x = x-50
y = y-50

mc.player.setTilePos(x,y,z)
time.sleep(2)

x = x-50
y = y-50

mc.player.setTilePos(x,y,z)