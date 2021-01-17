import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees


window = pyglet.window.Window(1280,720,"Pymunk Tester",resizable = False) # width,height,title,not resizble
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0,-1000 #gravity for x and y directions

'''Body types: (default is DYNAMIC)
    DYNAMIC: affected by gravity and other forces (ball,player,enemies etc)
    KINEMATIC: Not affected by gravity or other forces, but can be moved (platforms,doors)
    STATIC: Not affected by gravity or other forces, and cannot be moved (ground,building, immovable object)

   Moment of Inertia: How much a body will resist rotation. Large value: resists rotation/angular acceleration more'''


mass = 1
radius = 30
circle_moment = pymunk.moment_for_circle(mass,0,radius)
circle_body = pymunk.Body(mass,circle_moment)
circle_body.position = 200,500
circle_shape = pymunk.Circle(circle_body,radius)
circle_shape.elasticity = 0.8 #0 to 1
circle_shape.friction = 1 #0 - frictionless, >1 - perfectly fine

segment_shape = pymunk.Segment(space.static_body,(0,60),(800,0),2)
segment_shape.body.position = 100,100
segment_shape.elasticity = 0.8
segment_shape.friction = 1

space.add(circle_body, circle_shape,segment_shape)

#working with sprites:
sprite_img = pyglet.image.load("smile.png")
sprite_img.anchor_x = sprite_img.width // 2
sprite_img.anchor_y = sprite_img.height // 2
sprite = pyglet.sprite.Sprite(sprite_img,circle_body.position.x,circle_body.position.y)


@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    sprite.draw()
    

def update(dt):#param is time
    space.step(dt)
    sprite.position = circle_body.position
    sprite.rotation = degrees(-circle_body.angle)



if __name__=='__main__':
    pyglet.clock.schedule_interval(update, 1.0/60) #update method called every 1/60th of a second
    pyglet.app.run()