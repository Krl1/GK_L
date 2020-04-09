from OpenGL.GLUT import *
from OpenGL.GL import *

import numpy as np

MAX_STEP = 4

#Recursion(step=1, width=200.0, center=np.array([0.0,0.0]))

def New_Center_and_Draw(i, width, step, center):
    if i==0: #Lewy Górny
        curvature = NewCurvature() * (-1)
        new_center = center + [-width, width] + [0,width/2*curvature]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center

    if i==1: #Środkowy Górny
        curvature = NewCurvature() * (-1)
        new_center = center + [0.0, width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center

    if i==2: #Prawy Górny
        curvature = NewCurvature() * (-1)
        new_center = center + [+width, width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center

    if i==3: #Lewy Środkowy
        curvature = NewCurvature()
        new_center = center + [-width, 0.0]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center

    if i==5: #Prawy Środkowy
        curvature = NewCurvature()
        new_center = center + [+width, 0.0]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center

    if i==6: #Lewy Dolny
        curvature = NewCurvature()
        new_center = center + [-width, -width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center

    if i==7: #Środkowy Dolny
        curvature = NewCurvature()
        new_center = center + [0.0, -width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center

    if i==8: #Prawy Dolny
        curvature = NewCurvature()
        new_center = center + [+width, -width]
        IfMaxStepDraw(width, new_center, curvature, step)
        new_center += [0,width/2*curvature]
        return new_center


def Iteratively(step, width, center):
    step_1 = step
    width_1 = width
    center_1 = center + [0,width/2*NewCurvature()]
    for i_2 in range(9):
        if i_2 == 4:
            continue
        step_2 = step_1 +1
        width_2 = width_1/3
        center_2 = New_Center_and_Draw(i_2, width_2, step_2, center_1)
        for i_3 in range(9):
            if i_3 == 4:
                continue
            step_3 = step_2 +1
            width_3 = width_2/3
            center_3 = New_Center_and_Draw(i_3, width_3, step_3, center_2)
            for i_4 in range(9):
                if i_4 == 4:
                    continue
                step_4 = step_3 +1
                width_4 = width_3/3
                center_4 = New_Center_and_Draw(i_4, width_4, step_4, center_3)


def IfMaxStepDraw(width, new_center, curvature, step):
    if step == MAX_STEP:
        DrawColorPolygon(width, new_center, curvature)

def DrawWhitePolygon(width, center, curvature):
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(center[0]-0.5*width, center[1]+0.5*width)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(center[0]+0.5*width, center[1]+0.5*width+curvature*width)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(center[0]+0.5*width, center[1]-0.5*width+curvature*width)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(center[0]-0.5*width, center[1]-0.5*width)
    glEnd()

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
    Iteratively(step=1, width=200.0, center=np.array([0.0,0.0]))
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
