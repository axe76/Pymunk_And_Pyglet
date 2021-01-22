# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:49:25 2021

@author: ACER
"""
import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions


window = pyglet.window.Window(1280,720,"Pymunk Tester",resizable = False) # width,height,title,not resizble
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0,-1000 #gravity for x and y directions

'''Body types: (default is DYNAMIC)
    DYNAMIC: affected by gravity and other forces (ball,player,enemies etc)
    KINEMATIC: Not affected by gravity or other forces, but can be moved (platforms,doors)
    STATIC: Not affected by gravity or other forces, and cannot be moved (ground,building, immovable object)

   Moment of Inertia: How much a body will resist rotation. Large value: resists rotation/angular acceleration more'''

poly = pymunk.Poly.create_box(None,size = (50,50))
moment = pymunk.moment_for_poly(1,vertices=poly.get_vertices())

body = pymunk.Body(1,moment,pymunk.Body.DYNAMIC) #rigid body (without shape right now); params: mass, MOI
poly.body = body
body.position = 640,700

mass = 1
radius = 30
circle_moment = pymunk.moment_for_circle(mass,0,radius)
circle_body = pymunk.Body(mass,circle_moment)
circle_body.position = 100,700
circle_shape = pymunk.Circle(circle_body,radius)

segment_moment = pymunk.moment_for_segment(mass,(0,0),(0,400),2) #end points and thickness
segment_body = pymunk.Body(mass,segment_moment)
segment_body.position = 400,300
segment_shape = pymunk.Segment(segment_body,(0,0),(0,400),2)

triangle_shape = pymunk.Poly(None,((0,0),(100,0),(50,100)))
triangle_moment = pymunk.moment_for_poly(mass,triangle_shape.get_vertices())
traingle_body = pymunk.Body(mass,triangle_moment)
traingle_body.position = 700,700
triangle_shape.body = traingle_body

penta_shape = pymunk.Poly(None,((0,0),(100,0),(150,100),(50,200),(-50,100)))
penta_moment = pymunk.moment_for_poly(mass,penta_shape.get_vertices())
penta_body = pymunk.Body(mass,penta_moment)
penta_body.position = 900,700
penta_shape.body = penta_body

space.add(circle_body, circle_shape,body,poly,segment_body,segment_shape,traingle_body,triangle_shape,penta_body,penta_shape)

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    

def update(dt):#param is time
    space.step(dt)

#pyglet.app.exit()

if __name__=='__main__':
    pyglet.clock.schedule_interval(update, 1.0/60) #update method called every 1/60th of a second
    pyglet.app.run()
