import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees


window = pyglet.window.Window(1280,720,"Pymunk Tester",resizable = False) # width,height,title,not resizble
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0,-1000 #gravity for x and y directions

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
segment_shape.id = 1

space.add(circle_body, circle_shape,segment_shape)

#begin callback: called when 2 bodies begin contact
#pre and post are called during the contact phase
#separate called when contact ends
#so for ball falling on line segment and then rolling on it and then falling:
#starts with begin, then a series of pre and post during contact and ends with separate for each bounce and a final separate when it falls off

#Arbiter object: encapsulates a pair of colliding shapes and all of the data about their collision

def coll_begin(arbiter,space,data):
    print(arbiter.shapes)
    circle = arbiter.shapes[0]
    #here cirlce_shape  = arbiter.shapes[0] and object it collides with is arbiter.shapes[1], 
    # so here we can check if it collides with an object by checkind id of arbiter.shapes[1] like:
    '''if arbiter.shapes[1].id == required_id:
        space.remove(circle.body,circle)'''
    return True

def coll_pre(arbiter,space,data):
    #print('pre solve')
    return True

def coll_post(arbiter,space,data):
    #print('post solve')
    pass

def coll_separate(arbiter,space,data):
    #print('separate')
    pass

handler = space.add_default_collision_handler()
handler.begin = coll_begin
handler.pre_solve = coll_pre
handler.post_solve = coll_post
handler.separate = coll_separate

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)
    

def update(dt):#param is time
    space.step(dt)



if __name__=='__main__':
    pyglet.clock.schedule_interval(update, 1.0/60) #update method called every 1/60th of a second
    pyglet.app.run()