#1-3

#import
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 189
y = 76
z = 184

#teleport
mc.player.setTilePos(x, y, z)