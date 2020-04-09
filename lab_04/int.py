#  Szkielet programu do tworzenia modelu sceny 3-D z wizualizacją osi 
#  układu współrzednych

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import numpy as np
import sys

model = 1 #1- punkty, 2- siatka, 3 - wypełnione trójkąty, 4- GL_Triangle_STRIP
N=13
theta = [0.0, 0.0, 0.0]
viewer= [0.0, 0.0, 10.0]

def keys(key, x, y):
    global model
    global N
    if key == b'p' :    
        model = 1 
    if key == b'w' :    
        model = 2 
    if key == b's' :
        model = 3
    if key == b'r' :
        model = 4
    if key == b'q' :
        if N>2:
            N-=1
    if key == b'e' :
        if N<50:
            N+=1


def Egg():
    tab_xyz = np.zeros((N,N,3))
    for i in range(N):
        u = i/(N-1)
        for j in range(N):
            v = j/(N-1)
            tmp = (-90*u**5 + 225*u**4 - 270*u**3 + 180*u**2-45*u)
            tab_xyz[i,j,0]=tmp*np.cos(np.pi*v)
            tab_xyz[i,j,1]=160*u**4 - 320*u**3 + 160*u**2
            tab_xyz[i,j,2]=tmp*np.sin(np.pi*v)

    np.random.seed(1)
    tab_colours = np.random.rand(N,N,3)

    if model == 1:
        EggPoints(tab_xyz)
    if model == 2:
        EggNet(tab_xyz)
    if model == 3:
        EggTriangles(tab_xyz,tab_colours)
    if model == 4:
        EggTriangleStrip(tab_xyz,tab_colours)
    
def Axes():
    x_min = [-5.0, 0.0, 0.0]
    x_max = [5.0, 0.0, 0.0]
    # początek i koniec obrazu osi x

    y_min = [0.0, -5.0, 0.0]
    y_max = [0.0,  5.0, 0.0]
    # początek i koniec obrazu osi y

    z_min = [0.0, 0.0, -5.0]
    z_max = [0.0, 0.0,  5.0]
    # początek i koniec obrazu osi z
    
    glColor3f(1.0, 0.0, 0.0) # kolor rysowania osi - czerwony
    glBegin(GL_LINES) # rysowanie osi x
    glVertex3fv(x_min)
    glVertex3fv(x_max)
    glEnd()

    glColor3f(0.0, 1.0, 0.0) # kolor rysowania - zielony
    glBegin(GL_LINES) # rysowanie osi y

    glVertex3fv(y_min)
    glVertex3fv(y_max)                          
    glEnd()

    glColor3f(0.0, 0.0, 1.0) # kolor rysowania - niebieski
    glBegin(GL_LINES) # rysowanie osi z

    glVertex3fv(z_min)
    glVertex3fv(z_max)
    glEnd()

def RenderScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(viewer[0], viewer[1], viewer[2], 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    Axes()
    glColor3f(1.0, 1.0, 1.0) 
    # glRotated(30.0, 2.0, 0.0, 0.0)
    # glRotatef(theta[0], 1.0, 0.0, 0.0)
    # glRotatef(theta[1], 0.0, 1.0, 0.0)
    # glRotatef(theta[2], 0.0, 0.0, 1.0)
    glutWireTeapot(3.0) # Narysowanie obrazu czajnika do herbaty
    glFlush()
    glutSwapBuffers()

def MyInit():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    # Kolor czyszcący (wypełnienia okna) ustawiono na czarny
 
def ChangeSize(horizontal, vertical):
    glMatrixMode(GL_PROJECTION)
    # Przełączenie macierzy bieżącej na macierz projekcji
    glLoadIdentity()
    gluPerspective(70.0, 1.0, 1.0, 30.0)

    if(horizontal <= vertical):
        glViewport(0, (vertical-horizontal)/2, horizontal, horizontal)
    else:
        glViewport((horizontal-vertical)/2, 0, vertical, vertical)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():       
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(300, 300)
    glutCreateWindow("Rzutowanie perspektywiczne")           
    glutDisplayFunc(RenderScene)
    #glutKeyboardFunc(keys) 
    glutReshapeFunc(ChangeSize)
    MyInit()
    glEnable(GL_DEPTH_TEST)
    # glutIdleFunc(spinEgg)
    glutMainLoop()
    
main()