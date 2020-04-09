from OpenGL.GLUT import *
from OpenGL.GL import *

import numpy as np

MAX_STEP = 4


def Recursion(step, width, center):
    if step == 1:
        curvature = NewCurvature()
        #DrawColorPolygon(width, center, curvature)
        new_center = center + [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

    elif step <= MAX_STEP:
        #Lewy Górny
        curvature = NewCurvature() * (-1)
        new_center = center + [-width, width] + [0,width/2*curvature]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

        #Środkowy Górny
        curvature = NewCurvature() * (-1)
        new_center = center + [0.0, width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

        #Prawy Górny
        curvature = NewCurvature() * (-1)
        new_center = center + [+width, width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

        #Lewy Środkowy
        curvature = NewCurvature()
        new_center = center + [-width, 0.0]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

        #Prawy Środkowy
        curvature = NewCurvature()
        new_center = center + [+width, 0.0]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

        #Lewy Dolny
        curvature = NewCurvature()
        new_center = center + [-width, -width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

        #Środkowy Dolny
        curvature = NewCurvature()
        new_center = center + [0.0, -width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)

        #Prawy Dolny
        curvature = NewCurvature()
        new_center = center + [+width, -width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        Recursion(step+1, width/3.0, new_center)


def IfMaxStepDraw(width, new_center, curvature, step):
    if step == MAX_STEP:
        DrawColorPolygon(width, new_center, curvature)


def DrawColorPolygon(width, center, curvature):
    glBegin(GL_POLYGON)
    GetColor()
    glVertex2f(center[0]-0.5*width, center[1]+0.5*width)
    GetColor()
    glVertex2f(center[0]+0.5*width, center[1]+0.5*width+curvature*width)
    GetColor()
    glVertex2f(center[0]+0.5*width, center[1]-0.5*width+curvature*width)
    GetColor()
    glVertex2f(center[0]-0.5*width, center[1]-0.5*width)
    glEnd()

def NewCurvature():
    return np.random.random()/10

def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT)
    Recursion(step=1, width=200.0, center=np.array([0.0,0.0]))
    glFlush()

def GetColor():
    color = list(np.random.random(size=3))
    return glColor3f(color[0],color[1],color[2])

def MyInit():
    glClearColor(0.8, 0.8, 0.8, 1.0)

def ChangeSize(horizontal, vertical):
    if vertical<=100:
        vertical = 101

    #glClearColor( 1.0, 1.0, 1.0, 1.0 )
    glViewport(50, 50, horizontal-100, vertical-100)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    AspectRatio = horizontal/vertical

    width=200.0

    if(horizontal <= vertical):
        glOrtho(-width/2,width/2,-width/2/AspectRatio,width/2/AspectRatio,1.0,-1.0)
    else:
        glOrtho(-width/2*AspectRatio,width/2*AspectRatio,-width/2,width/2,1.0,-1.0)

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutCreateWindow("Fraktal")
    glutDisplayFunc(RenderScene)
    glutReshapeFunc(ChangeSize)
    MyInit()
    glutMainLoop()

main()
