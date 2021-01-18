import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees


window = pyglet.window.Window(1280,720,"Pymunk Tester",resizable = False) # width,height,title,not resizble
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0,-1000 #gravity for x and y directions

sprite_batch = pyglet.graphics.Batch()

'''Body types: (default is DYNAMIC)
    DYNAMIC: affected by gravity and other forces (ball,player,enemies etc)
    KINEMATIC: Not affected by gravity or other forces, but can be moved (platforms,doors)
    STATIC: Not affected by gravity or other forces, and cannot be moved (ground,building, immovable object)

   Moment of Inertia: How much a body will resist rotation. Large value: resists rotation/angular acceleration more'''


mass = 1
radius = 30

segment_shape = pymunk.Segment(space.static_body,(0,60),(800,0),2)
segment_shape.body.position = 100,100
segment_shape.elasticity = 0.8
segment_shape.friction = 1

space.add(segment_shape)

#working with sprites:
sprite_img = pyglet.image.load("smile.png")
sprite_img.anchor_x = sprite_img.width // 2
sprite_img.anchor_y = sprite_img.height // 2
#sprite = pyglet.sprite.Sprite(sprite_img,circle_body.position.x,circle_body.position.y)

sprites_click = [] #list of sprites  added on click


@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    #sprite.draw()
    sprite_batch.draw()
    
#adding bodies on location of click
@window.event
def on_mouse_press(x,y,button,modifiers):
    circle_moment_click = pymunk.moment_for_circle(mass,0,radius)
    circle_body_click = pymunk.Body(mass,circle_moment_click)
    circle_body_click.position = x,y
    circle_shape_click = pymunk.Circle(circle_body_click,radius)
    circle_shape_click.elasticity = 0.8 #0 to 1
    circle_shape_click.friction = 1 #0 - frictionless, >1 - perfectly fine
    sprites_click.append(pyglet.sprite.Sprite(sprite_img,circle_body_click.position.x,circle_body_click.position.y,batch = sprite_batch))
    space.add(circle_body_click, circle_shape_click)

def update(dt):#param is time
    space.step(dt)

    for index,sprite_ in enumerate(sprites_click):
        sprite_.rotation = degrees(-space.bodies[index].angle) #index +1 as we have already created one body and shape outside of click function as default
        sprite_.position = space.bodies[index].position

        for shape in space.shapes:
            if shape.body.position.y < -100:
                sprites_click.remove(sprite_)
                space.remove(shape.body,shape)




if __name__=='__main__':
    pyglet.clock.schedule_interval(update, 1.0/60) #update method called every 1/60th of a second
    pyglet.app.run()