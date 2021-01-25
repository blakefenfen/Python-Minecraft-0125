#1-6

#install
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

mc.postToChat("I'm watching you bro!")

while True:
    x,y,z, = mc.player.getTilePos()
    mc.postToChat("您現在的位置:X"+str(x)+" Y:"+str(y)+" Z:"+str(z))
    time.sleep(1)