#1-5

#Install
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

i = 0
while True:
    i = i+1
    mc.postToChat("第"+str(i)+"次測試")
    time.sleep(1)