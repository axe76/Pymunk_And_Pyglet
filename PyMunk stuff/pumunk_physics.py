# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:58:59 2021

@author: ACER
"""

import pymunk
import time

space = pymunk.Space()
space.gravity = 0,-1000 #gravity for x and y directions

body = pymunk.Body(1,1666) #rigid body (without shape right now); params: mass, MOI
body.position = 50,100

space.add(body)

while True:
    space.step(0.02) # 1/50 i.e 50 frames per second
    print(body.position)
    time.sleep(0.5)
    


