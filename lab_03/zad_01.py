#  Szkielet programu do tworzenia modelu sceny 3-D z wizualizacją osi 
#  układu współrzednych

from OpenGL.GLUT import *
from OpenGL.GL import *

import numpy as np
import sys

model = 1 #1- punkty, 2- siatka, 3 - wypełnione trójkąty, 4- GL_Triangle_STRIP
N=10
theta = [0.0, 0.0, 0.0]

def spinEgg():
	theta[0] -= .5
	if theta[0] > 360.0: theta[0] -= 360.0
	theta[1] -= .5
	if theta[1] > 360.0: theta[1] -= 360.0
	theta[2] -= .5
	if theta[2] > 360.0: theta[2] -= 360.0
	glutPostRedisplay()

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

def EggNet(tab_xyz):
	glBegin(GL_LINES)
	for i in range(N):
		for j in range(N-1):
			x_1=tab_xyz[i,j,0]
			y_1=tab_xyz[i,j,1]-5
			z_1=tab_xyz[i,j,2]
			glVertex3f(x_1,y_1,z_1)
			x_2=tab_xyz[i,j+1,0]
			y_2=tab_xyz[i,j+1,1]-5
			z_2=tab_xyz[i,j+1,2]
			glVertex3f(x_2,y_2,z_2)

	for i in range(N-1):
		for j in range(N):
			x_1=tab_xyz[i,j,0]
			y_1=tab_xyz[i,j,1]-5
			z_1=tab_xyz[i,j,2]
			glVertex3f(x_1,y_1,z_1)
			x_2=tab_xyz[i+1,j,0]
			y_2=tab_xyz[i+1,j,1]-5
			z_2=tab_xyz[i+1,j,2]
			glVertex3f(x_2,y_2,z_2)

	glEnd()		

def EggTriangles(tab_xyz, tab_colours):
	glBegin(GL_TRIANGLES)

	for i in range(N-1):
		for j in range(N-1):
			glColor3f(tab_colours[i,j,0], tab_colours[i,j,1], tab_colours[i,j,2])
			x_1=tab_xyz[i,j,0]
			y_1=tab_xyz[i,j,1]-5
			z_1=tab_xyz[i,j,2]
			glVertex3f(x_1,y_1,z_1)

			glColor3f(tab_colours[i,j+1,0], tab_colours[i,j+1,1], tab_colours[i,j+1,2])
			x_2=tab_xyz[i,j+1,0]
			y_2=tab_xyz[i,j+1,1]-5
			z_2=tab_xyz[i,j+1,2]
			glVertex3f(x_2,y_2,z_2)

			glColor3f(tab_colours[i+1,j,0], tab_colours[i+1,j,1], tab_colours[i+1,j,2])
			x_3=tab_xyz[i+1,j,0]
			y_3=tab_xyz[i+1,j,1]-5
			z_3=tab_xyz[i+1,j,2]
			glVertex3f(x_3,y_3,z_3)

			if j == N-2:
				glColor3f(tab_colours[i,0,0], tab_colours[i,0,1], tab_colours[i,0,2])
			else:
				glColor3f(tab_colours[i,j+1,0], tab_colours[i,j+1,1], tab_colours[i,j+1,2])
			x_1=tab_xyz[i,j+1,0]
			y_1=tab_xyz[i,j+1,1]-5
			z_1=tab_xyz[i,j+1,2]
			glVertex3f(x_1,y_1,z_1)

			glColor3f(tab_colours[i+1,j,0], tab_colours[i+1,j,1], tab_colours[i+1,j,2])
			x_2=tab_xyz[i+1,j,0]
			y_2=tab_xyz[i+1,j,1]-5
			z_2=tab_xyz[i+1,j,2]
			glVertex3f(x_2,y_2,z_2)

			if j == N-2:
				glColor3f(tab_colours[i+1,0,0], tab_colours[i+1,0,1], tab_colours[i+1,0,2])
			else:
				glColor3f(tab_colours[i+1,j+1,0], tab_colours[i+1,j+1,1], tab_colours[i+1,j+1,2])
			x_3=tab_xyz[i+1,j+1,0]
			y_3=tab_xyz[i+1,j+1,1]-5
			z_3=tab_xyz[i+1,j+1,2]
			glVertex3f(x_3,y_3,z_3)
			
	glEnd()

def EggTriangleStrip(tab_xyz,tab_colours):
	glBegin(GL_TRIANGLE_STRIP)

	for i in range(N-1):
		glColor3f(tab_colours[i,0,0], tab_colours[i,0,1], tab_colours[i,0,2])
		x_1=tab_xyz[i,0,0]
		y_1=tab_xyz[i,0,1]-5
		z_1=tab_xyz[i,0,2]
		glVertex3f(x_1,y_1,z_1)

		glColor3f(tab_colours[i,1,0], tab_colours[i,1,1], tab_colours[i,1,2])
		x_2=tab_xyz[i,1,0]
		y_2=tab_xyz[i,1,1]-5
		z_2=tab_xyz[i,1,2]
		glVertex3f(x_2,y_2,z_2)	
		for j in range(0,N-2,2):
			glColor3f(tab_colours[i+1,j,0], tab_colours[i+1,j,1], tab_colours[i+1,j,2])
			x_3=tab_xyz[i+1,j,0]
			y_3=tab_xyz[i+1,j,1]-5
			z_3=tab_xyz[i+1,j,2]
			glVertex3f(x_3,y_3,z_3)

			glColor3f(tab_colours[i+1,j+1,0], tab_colours[i+1,j+1,1], tab_colours[i+1,j+1,2])
			x_3=tab_xyz[i+1,j+1,0]
			y_3=tab_xyz[i+1,j+1,1]-5
			z_3=tab_xyz[i+1,j+1,2]
			glVertex3f(x_3,y_3,z_3)
		
			glColor3f(tab_colours[i+1,j+2,0], tab_colours[i+1,j+2,1], tab_colours[i+1,j+2,2])
			x_3=tab_xyz[i+1,j+2,0]
			y_3=tab_xyz[i+1,j+2,1]-5
			z_3=tab_xyz[i+1,j+2,2]
			glVertex3f(x_3,y_3,z_3)

			glColor3f(tab_colours[i,j+1,0], tab_colours[i,j+1,1], tab_colours[i,j+1,2])
			x_2=tab_xyz[i,j+1,0]
			y_2=tab_xyz[i,j+1,1]-5
			z_2=tab_xyz[i,j+1,2]
			glVertex3f(x_2,y_2,z_2)	

			glColor3f(tab_colours[i,j+2,0], tab_colours[i,j+2,1], tab_colours[i,j+2,2])
			x_3=tab_xyz[i,j+2,0]
			y_3=tab_xyz[i,j+2,1]-5
			z_3=tab_xyz[i,j+2,2]
			glVertex3f(x_3,y_3,z_3)

			if j != N-3:
				if j == N-4:
					glColor3f(tab_colours[i,0,0], tab_colours[i,0,1], tab_colours[i,0,2])
				else:
					glColor3f(tab_colours[i,j+3,0], tab_colours[i,j+3,1], tab_colours[i,j+3,2])
				x_3=tab_xyz[i,j+3,0]
				y_3=tab_xyz[i,j+3,1]-5
				z_3=tab_xyz[i,j+3,2]
				glVertex3f(x_3,y_3,z_3)

			if j == N-4 :
				glColor3f(tab_colours[i+1,j+2,0], tab_colours[i+1,j+2,1], tab_colours[i+1,j+2,2])
				x_3=tab_xyz[i+1,j+2,0]
				y_3=tab_xyz[i+1,j+2,1]-5
				z_3=tab_xyz[i+1,j+2,2]
				glVertex3f(x_3,y_3,z_3)

				glColor3f(tab_colours[i+1,0,0], tab_colours[i+1,0,1], tab_colours[i+1,0,2])
				x_3=tab_xyz[i+1,j+3,0]
				y_3=tab_xyz[i+1,j+3,1]-5
				z_3=tab_xyz[i+1,j+3,2]
				glVertex3f(x_3,y_3,z_3)

	glEnd()

def EggPoints(tab_xyz):
	glBegin(GL_POINTS)
	for i in range(N):
		for j in range(N):
			x=tab_xyz[i,j,0]
			y=tab_xyz[i,j,1]-5
			z=tab_xyz[i,j,2]
			glVertex3f(x,y,z)
	glEnd()		

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
	Axes()
	glColor3f(1.0, 1.0, 1.0) 
	glRotated(30.0, 2.0, 0.0, 0.0)
	glRotatef(theta[0], 1.0, 0.0, 0.0)
	glRotatef(theta[1], 0.0, 1.0, 0.0)
	glRotatef(theta[2], 0.0, 0.0, 1.0)
	Egg()
	glFlush()
	glutSwapBuffers()

def MyInit():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	# Kolor czyszcący (wypełnienia okna) ustawiono na czarny
 
def ChangeSize(horizontal, vertical):
	# Deklaracja zmiennej AspectRatio  określającej proporcję
	# wymiarów okna 
	if vertical == 0:  # Zabezpieczenie przed dzieleniem przez 0
		vertical = 1  
	glViewport(0, 0, horizontal, vertical)
	# Ustawienie wielkościokna okna widoku (viewport)
	# W tym przypadku od (0,0) do (horizontal, vertical)  
	glMatrixMode(GL_PROJECTION)
	# Przełączenie macierzy bieżącej na macierz projekcji 
	glLoadIdentity()
	# Czyszcznie macierzy bieżącej            
	AspectRatio = horizontal/ vertical
	# Wyznaczenie współczynnika  proporcji okna
	# Gdy okno nie jest kwadratem wymagane jest określenie tak zwanej
	# przestrzeni ograniczającej pozwalającej zachować właściwe
	# proporcje rysowanego obiektu.
	# Do okreslenia przestrzeni ograniczjącej służy funkcja
	# glOrtho(...)            
	if horizontal <= vertical:
		glOrtho(-7.5,7.5,-7.5/AspectRatio,7.5/AspectRatio,10.0, -10.0) 
	else:
		glOrtho(-7.5*AspectRatio,7.5*AspectRatio,-7.5,7.5,10.0,-10.0)                     
	
	glMatrixMode(GL_MODELVIEW)
	# Przełączenie macierzy bieżącej na macierz widoku modelu                                   

	glLoadIdentity()
	# Czyszcenie macierzy bieżącej

def main():       
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(300, 300)
	glutCreateWindow("Uklad wspolrzednych 3-D")           
	glutDisplayFunc(RenderScene)
	glutKeyboardFunc(keys) 
	glutReshapeFunc(ChangeSize)
	MyInit()
	glEnable(GL_DEPTH_TEST)
	glutIdleFunc(spinEgg)
	glutMainLoop()
	
main()