from gl import Raytracer, V3
from texture import *
from figures import *
from lights import *


width = 256
height = 256


def BoxGenerator(position=V3(0,0,0), size=0.5, rtx=None, material=None):
    x = position.x
    y = position.y
    z = position.z
    
    rtx.scene.append( AABB(V3(x,y-(size/2),z), V3(size,0,size), material) )
    rtx.scene.append( AABB(V3(x,y+(size/2),z), V3(size,0,size), material) )
    rtx.scene.append( AABB(V3(x-(size/2),y,z), V3(0,size,size), material) )
    rtx.scene.append( AABB(V3(x+(size/2),y,z), V3(0,size,size), material) )
    rtx.scene.append( AABB(V3(x,y,z-(size/2)), V3(size,size,0), material) )
    rtx.scene.append( AABB(V3(x,y,z+(size/2)), V3(size,size,0), material) )







# Materiales
paredes = Material(diffuse = (0.4, 0.4, 0.4), spec = 32)
Techo = Material(diffuse = (0.45, 0.45, 0.45), spec = 32)
paredFondo = Material(diffuse = (0.3, 0.3, 0.3), spec = 32)
piso = Material(diffuse = (0.7, 0.7, 0.7), spec = 64, matType = REFLECTIVE)

mat1 = Material(diffuse = (0.9, 0.9, 0.2), spec = 64)
mat2 = Material(diffuse = (0.9, 0.2, 0.2), spec = 64)
mat3 = Material(diffuse = (0.2, 0.2, 0.9), spec = 64)


rtx = Raytracer(width, height)


rtx.lights.append( AmbientLight(intensity = 0.6 ))
rtx.lights.append( PointLight(point = (0,0,-2) ))

# Room
rtx.scene.append( AABB(V3(0,-3,-8), V3(6,0.1,8), piso) )
rtx.scene.append( AABB(V3(0,3,-8), V3(6,0.1,8), piso) )
rtx.scene.append( AABB(V3(-3,0,-8), V3(0.1,6,8), paredes) )
rtx.scene.append( AABB(V3(3,0,-8), V3(0.1,6,8), paredes) )
rtx.scene.append( AABB(V3(0,0,-8), V3(6,6,0.1), paredFondo) )


# Box 1
BoxGenerator(V3(2,-2,-7), 0.5, rtx, mat1)

# Box 2
BoxGenerator(V3(-2,2,-7), 0.5, rtx, mat2)

rtx.glRender()

rtx.glFinish("output.bmp")