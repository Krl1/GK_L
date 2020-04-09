#  Szkielet programu do tworzenia modelu sceny 3-D z wizualizacją osi 
#  układu współrzednych

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import sys
from math import fabs

function = 0

position = [[-20.0, 0.0, 10.0],[20.0, 0.0, 10.0]]
pix2angle = 0.0
status=0

x_pos_old = [0,0]
delta_x = [0,0]
y_pos_old = [0,0]
delta_y = [0,0]


viewer = [[1.0, 1.0, 10.0],[10.0, 1.0, 1.0],[1.0, 10.0, 1.0]]
center = [[0.0, 0.0, 0.0],[0.0, 0.0, 0.0],[0.0, 0.0, 0.0]]

    
def Axes():
    x_min = [-5.0, 0.0, 0.0]
    x_max = [5.0, 0.0, 0.0]
    y_min = [0.0, -5.0, 0.0]
    y_max = [0.0,  5.0, 0.0]
    z_min = [0.0, 0.0, -5.0]
    z_max = [0.0, 0.0,  5.0]
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
    global theta, viewer, position
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(viewer[function][0], viewer[function][1], viewer[function][2], center[function][0], center[function][1], center[function][2], .0, 1.0, 0.0)
    Axes()

    if(status > 0):
        R = np.sqrt((position[status-1][0]-center[function][0])**2 + (position[status-1][1]-center[function][1])**2 + (position[status-1][2]-center[function][2])**2 )
        elewacja = np.arcsin(position[status-1][1]/R)
        azymut = np.arccos(position[status-1][0]/(R*np.cos(elewacja)))

        elewacja += (delta_x[status-1] * pix2angle)/50
        azymut += (delta_y[status-1] * pix2angle)/50
  
        position[status-1][0] = R*np.cos(azymut)*np.cos(elewacja)
        position[status-1][1] = R*np.sin(elewacja)
        position[status-1][2] = R*np.sin(azymut)*np.cos(elewacja)
        
    glRotatef(0.0, 1.0, 0.0, 0.0)
    glRotatef(0.0, 0.0, 1.0, 0.0)
    glScale(1.0, 1.0, 1.0)
    glColor3f(1.0, 1.0, 1.0) 
    glutSolidTeapot(3.0)
    glTranslated(position[0][0], position[0][1], position[0][2])
    glutSolidTetrahedron()
    glTranslated(position[1][0]-position[0][0], position[1][1]-position[0][1], position[1][2]-position[0][2])
    glutWireOctahedron()
    MyInit()
    glFlush()
    glutSwapBuffers()

def MyInit():
    glClearColor(0.8, 0.8, 0.8, 1.0)
    mat_ambient  = [1.0, 1.0, 1.0, 1.0]
    mat_diffuse  = [fabs(position[0][0])/23, fabs(position[0][1])/23, fabs(position[0][2])/23, 1.0]
    mat_diffuse_1  = [fabs(position[1][0])/23, fabs(position[1][1])/23, fabs(position[1][2])/23, 1.0]
    mat_specular = [1.0, 1.0, 1.0, 1.0]
    mat_shininess  = 20.0
    light_position = [position[0][0], position[0][1], position[0][2], 1.0]   
    light_position_1 = [position[1][0], position[1][1], position[1][2], 1.0]  
    light_ambient = [0.1, 0.1, 0.1, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]       
    light_specular= [1.0, 1.0, 0.0, 1.0]
    att_constant  = 1.0
    att_linear    = 0.05
    att_quadratic  = 0.001
    
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialf(GL_FRONT, GL_SHININESS, mat_shininess)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular)
    glLightfv(GL_LIGHT1, GL_POSITION, light_position_1)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, att_constant)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, att_linear)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, att_quadratic)

    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHTING)  
    glEnable(GL_LIGHT0)    
    glEnable(GL_LIGHT1)    
    glEnable(GL_DEPTH_TEST)

 
def ChangeSize(horizontal, vertical):
    global pix2angle
    pix2angle = 360.0/float(horizontal)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(70.0, 1.0, 1.0, 30.0)

    if(horizontal <= vertical):
        glViewport(0, int((vertical-horizontal)/2), horizontal, horizontal)
    else:
        glViewport(int((horizontal-vertical)/2), 0, vertical, vertical)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def Mouse(btn, state, x, y):
    global status, x_pos_old, y_pos_old
    if btn==GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        x_pos_old[0] = x
        y_pos_old[0] = y
        status = 1
    elif btn==GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        x_pos_old[1] = x
        y_pos_old[1] = y
        status = 2
    else:
        status = 0
    
def Motion(x, y):
    global delta_x, x_pos_old, delta_y, y_pos_old
    for i in [0,1]:
        delta_x[i] = x -x_pos_old[i]
        x_pos_old[i] = x
        delta_y[i] = y - y_pos_old[i]
        y_pos_old[i] = y

    glutPostRedisplay()

def keys(key, x, y):
    global function
    if key == b'q':
        function += 1
        function = function%3

def main():       
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(300, 300)
    glutCreateWindow("Rzutowanie perspektywiczne")           
    glutDisplayFunc(RenderScene)
    glutKeyboardFunc(keys) 
    glutMouseFunc(Mouse)
    glutMotionFunc(Motion)
    glutReshapeFunc(ChangeSize)
    MyInit()
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()
    
main()