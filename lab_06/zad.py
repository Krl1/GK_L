import pygame
import sys
import time
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

nazwa = 'kot.png'
N=20
model = 1

def loadTexture():
	textureSurface = pygame.image.load(nazwa)
	textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
	width = textureSurface.get_width()
	height = textureSurface.get_height()
	
	glEnable(GL_CULL_FACE)
	glEnable(GL_TEXTURE_2D)
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

	glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)






def draw():
	glBegin(GL_TRIANGLES)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(1.0, 0.0)
	glVertex3f(1.0, -1.0,  1.0)
	glTexCoord2f(0.5, 1.0)
	glVertex3f(0.0,  1.0,  1.0)
	glEnd()


def draw_cube():
	glBegin(GL_QUADS)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(1.0, 0.0)
	glVertex3f(1.0, -1.0,  1.0)
	glTexCoord2f(1.0, 1.0)
	glVertex3f(1.0,  1.0,  1.0)
	glTexCoord2f(0.0, 1.0)
	glVertex3f(-1.0,  1.0,  1.0)
	glTexCoord2f(1.0, 0.0)
	glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(1.0, 1.0)
	glVertex3f(-1.0,  1.0, -1.0)
	glTexCoord2f(0.0, 1.0)
	glVertex3f(1.0,  1.0, -1.0)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(1.0, -1.0, -1.0)
	glTexCoord2f(0.0, 1.0)
	glVertex3f(-1.0,  1.0, -1.0)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(-1.0,  1.0,  1.0)
	glTexCoord2f(1.0, 0.0)
	glVertex3f(1.0,  1.0,  1.0)
	glTexCoord2f(1.0, 1.0)
	glVertex3f(1.0,  1.0, -1.0)
	glTexCoord2f(1.0, 1.0)
	glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(0.0, 1.0)
	glVertex3f(1.0, -1.0, -1.0)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(1.0, -1.0,  1.0)
	glTexCoord2f(1.0, 0.0)
	glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(1.0, 0.0)
	glVertex3f(1.0, -1.0, -1.0)
	glTexCoord2f(1.0, 1.0)
	glVertex3f(1.0,  1.0, -1.0)
	glTexCoord2f(0.0, 1.0)
	glVertex3f(1.0,  1.0,  1.0)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(1.0, -1.0,  1.0)
	glTexCoord2f(0.0, 0.0)
	glVertex3f(-1.0, -1.0, -1.0)
	glTexCoord2f(1.0, 0.0)
	glVertex3f(-1.0, -1.0,  1.0)
	glTexCoord2f(1.0, 1.0)
	glVertex3f(-1.0,  1.0,  1.0)
	glTexCoord2f(0.0, 1.0)
	glVertex3f(-1.0,  1.0, -1.0)
	glEnd()

def draw_jajo():
	tab_xyz = np.zeros((N,N,3))
	for i in range(N):
		u = i/(N-1)
		for j in range(N):
			v = j/(N-1)
			tmp = (-90*u**5 + 225*u**4 - 270*u**3 + 180*u**2-45*u)
			tab_xyz[i,j,0]=(tmp*np.cos(np.pi*v))/5
			tab_xyz[i,j,1]=(160*u**4 - 320*u**3 + 160*u**2)/5
			tab_xyz[i,j,2]=(tmp*np.sin(np.pi*v))/5

	np.random.seed(1)
	tab_colours = np.random.rand(N,N,3)
	
	glBegin(GL_TRIANGLES)
	for i in range(N-1):
		for j in range(N-1):
			glColor3f(tab_colours[i,j,0], tab_colours[i,j,1], tab_colours[i,j,2])
			x_1=tab_xyz[i,j,0]
			y_1=tab_xyz[i,j,1]-1
			z_1=tab_xyz[i,j,2]
			
			glColor3f(tab_colours[i,j+1,0], tab_colours[i,j+1,1], tab_colours[i,j+1,2])
			x_2=tab_xyz[i,j+1,0]
			y_2=tab_xyz[i,j+1,1]-1
			z_2=tab_xyz[i,j+1,2]
			
			glColor3f(tab_colours[i+1,j,0], tab_colours[i+1,j,1], tab_colours[i+1,j,2])
			x_3=tab_xyz[i+1,j,0]
			y_3=tab_xyz[i+1,j,1]-1
			z_3=tab_xyz[i+1,j,2]
			if i<N/2:
				glTexCoord2f(x_1,y_1/2+0.5)
				glVertex3f(x_1,y_1,z_1)

				glTexCoord2f(x_2,y_2/2+0.5)
				glVertex3f(x_2,y_2,z_2)

				glTexCoord2f(x_3,y_3/2+0.5)
				glVertex3f(x_3,y_3,z_3)

			else:
				glTexCoord2f(x_1,y_1/2+0.5)
				glVertex3f(x_1,y_1,z_1)

				glTexCoord2f(x_3,y_3/2+0.5)
				glVertex3f(x_3,y_3,z_3)

				glTexCoord2f(x_2,y_2/2+0.5)
				glVertex3f(x_2,y_2,z_2)
					

			if j == N-2:
				glColor3f(tab_colours[i,0,0], tab_colours[i,0,1], tab_colours[i,0,2])
			else:
				glColor3f(tab_colours[i,j+1,0], tab_colours[i,j+1,1], tab_colours[i,j+1,2])
			x_1=tab_xyz[i,j+1,0]
			y_1=tab_xyz[i,j+1,1]-1
			z_1=tab_xyz[i,j+1,2]

			glColor3f(tab_colours[i+1,j,0], tab_colours[i+1,j,1], tab_colours[i+1,j,2])
			x_2=tab_xyz[i+1,j,0]
			y_2=tab_xyz[i+1,j,1]-1
			z_2=tab_xyz[i+1,j,2]

			if j == N-2:
				glColor3f(tab_colours[i+1,0,0], tab_colours[i+1,0,1], tab_colours[i+1,0,2])
			else:
				glColor3f(tab_colours[i+1,j+1,0], tab_colours[i+1,j+1,1], tab_colours[i+1,j+1,2])
			x_3=tab_xyz[i+1,j+1,0]
			y_3=tab_xyz[i+1,j+1,1]-1
			z_3=tab_xyz[i+1,j+1,2]

			if i<N/2:
				glTexCoord2f(x_1,y_1/2+0.5)
				glVertex3f(x_1,y_1,z_1)

				glTexCoord2f(x_3,y_3/2+0.5)
				glVertex3f(x_3,y_3,z_3)

				glTexCoord2f(x_2,y_2/2+0.5)
				glVertex3f(x_2,y_2,z_2)

			else:
				glTexCoord2f(x_1,y_1/2+0.5)
				glVertex3f(x_1,y_1,z_1)

				glTexCoord2f(x_2,y_2/2+0.5)
				glVertex3f(x_2,y_2,z_2)

				glTexCoord2f(x_3,y_3/2+0.5)
				glVertex3f(x_3,y_3,z_3)
				
	glEnd()



def keys():
	global model, nazwa
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1: 
				nazwa = 'kot.png' 
			if event.key == pygame.K_2:
				nazwa = 'pies.png' 
			if event.key == pygame.K_3:
				nazwa = 'kotopies.png' 
			if event.key == pygame.K_q:
				model += 1
				model = model%3

def renderScene():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glRotated(1.0, 1.0, 1.0, 0.0)
	glRotatef(0.1, 1.0, 0.0, 0.0)
	glRotatef(0.1, 0.0, 1.0, 0.0)
	glRotatef(0.1, 0.0, 0.0, 1.0)
	if model == 1:
		draw()
	elif model == 2:
		draw_cube()
	else :
		draw_jajo()

def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT)	
	gluPerspective(45, display[0] / display[1], 0.1, 50.0)
	glTranslatef(0.0, 0.0, -5)

	while True:
		loadTexture()
		keys()
		renderScene()
		
		time.sleep(0.01)
		pygame.display.flip()

main()