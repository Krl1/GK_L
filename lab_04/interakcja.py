#  Szkielet programu do tworzenia modelu sceny 3-D z wizualizacją osi 
#  układu współrzednych

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
import sys

function = 0

theta = [0.0, 0.0, 1.0]
pix2angle = 0.0
status=0
x_pos_old = 0
delta_x = 0
y_pos_old = 0
delta_y = 0
zoom_pos_old = 1
delta_zoom = 1
viewer = [1.0, 1.0, 10.0]
center = [0.0, 0.0, 0.0]
	
def Axes():
	x_min = [-5.0, 0.0, 0.0]
	x_max = [5.0, 0.0, 0.0]
	y_min = [0.0, -5.0, 0.0]
	y_max = [0.0,  5.0, 0.0]
	z_min = [0.0, 0.0, -5.0]
	z_max = [0.0, 0.0,  5.0]
	
	glColor3f(1.0, 0.0, 0.0)
	glBegin(GL_LINES)	
	glVertex3fv(x_min)
	glVertex3fv(x_max)
	glEnd()

	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)

	glVertex3fv(y_min)
	glVertex3fv(y_max)                          
	glEnd()

	glColor3f(0.0, 0.0, 1.0)
	glBegin(GL_LINES)

	glVertex3fv(z_min)
	glVertex3fv(z_max)
	glEnd()

def RenderScene():
	global theta, viewer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	gluLookAt(viewer[0], viewer[1], viewer[2], center[0], center[1], center[2], .0, 1.0, 0.0)
	Axes()
	
	if(status == 1 and function == 0):
		theta[0] += delta_x * pix2angle
		theta[1] += delta_y * pix2angle
	elif(status == 2):
		theta[2] += (delta_zoom * pix2angle)/300
		max_r = 65
		R = np.sqrt((viewer[0]-center[0])**2 + (viewer[1]-center[1])**2 + (viewer[2]-center[2])**2 )
		if R * theta[2] > 65:
			theta[2] = max_r/R 
		elif R*theta[2] <1:
			theta[2] = 1/R
	elif(status == 1 and function == 1):
		R = np.sqrt((viewer[0]-center[0])**2 + (viewer[1]-center[1])**2 + (viewer[2]-center[2])**2 )
		elewacja = np.arcsin(viewer[1]/R)
		azymut = np.arccos(viewer[0]/(R*np.cos(elewacja)))

		elewacja += (delta_x * pix2angle)/150
		azymut += (delta_y * pix2angle)/150


		viewer[1] = R*np.cos(azymut)*np.cos(elewacja)
		viewer[0] = R*np.sin(elewacja)
		viewer[2] = R*np.sin(azymut)*np.cos(elewacja)


	glRotatef(theta[1], 1.0, 0.0, 0.0)
	glRotatef(theta[0], 0.0, 1.0, 0.0)
	glScale(theta[2],theta[2],theta[2])
	glColor3f(1.0, 1.0, 1.0) 
	glutWireTeapot(3.0)
	glFlush()
	glutSwapBuffers()

def MyInit():
	glClearColor(0.0, 0.0, 0.0, 1.0)
 
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
	global status, x_pos_old, y_pos_old, zoom_pos_old
	if btn==GLUT_LEFT_BUTTON and state == GLUT_DOWN:
		x_pos_old = x
		y_pos_old = y
		status = 1
	elif btn==GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
		zoom_pos_old = x
		status = 2
	else:
		status = 0
	


def Motion(x, y):
	global delta_x, x_pos_old, delta_y, y_pos_old, delta_zoom, zoom_pos_old
	delta_x = x - x_pos_old
	x_pos_old = x
	delta_y = y - y_pos_old
	y_pos_old = y
	delta_zoom = x - zoom_pos_old
	zoom_pos_old = x
	glutPostRedisplay()

def keys(key, x, y):
	global function
	if key == b'q':
		function += 1
		function = function%2
	if key == b'w':
		function = 2
	if key == b's':
		function = 3
	if key == b'a':
		function = 4
	if key == b'd':
		function = 5

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



#import pdb; pdb.set_trace()