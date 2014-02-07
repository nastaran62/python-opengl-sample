from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys
from numpy import *
from time import *

class Drawing():
  def __init__(self):
	  glClearColor(0.0, 0.0, 0.0, 0.0)
	  glShadeModel(GL_SMOOTH)
	  self.xrot = 0
	  self.yrot = 0
	  self.zrot = 0
	  self.axrange = 10.0
	  self.spin = 0.0
	  gluLookAt(-10.0,-10.0,0.0,0.0,1.0,0.0,0.0,0.0,10.0)
	  glOrtho(-self.axrange, self.axrange, -self.axrange, self.axrange, -self.axrange, self.axrange)
	  self.lighting()
	  
  def plot_axises(self):
	  glBegin(GL_LINES)
	  glColor3f(1.0,1.0,1.0)
	  glVertex3f(-self.axrange, 0.0, 0.0)
	  glVertex3f(self.axrange,0.0, 0.0)
	  glVertex3f(0.0, self.axrange, 0.0)
	  glVertex3f(0.0, -self.axrange, 0.0)
	  glVertex3f(0.0, 0.0 , -self.axrange)
	  glVertex3f(0.0, 0.0, self.axrange)
	  glEnd()

  def keyboard(self,key,x,y):
	  if key == chr(27) or key == 'q' or key == 'Q':
		  sys.exit()
		  
	  if key == 'x' :
		  self.xrot += 5.0
	  if key == 'a' :
		  self.xrot -= 5.0
	  if key == 'y' :
		  self.yrot += 5.0
	  if key == 'b' :
		  self.yrot -= 5.0
	  if key == 'z':
		  self.zrot += 5.0
	  if key == 'c' :
		  self.zrot -= 5.0
	  glutPostRedisplay()

  def rotate_translate(self):
	  glRotatef(self.xrot, 1.0, 0.0, 0.0)
	  glRotatef(self.yrot, 0.0, 1.0, 0.0)
	  glRotatef(self.zrot, 0.0, 0.0, 1.0)

  def mouse(self, button, state, x , y):
	  if button == GLUT_LEFT_BUTTON :
		  if state == GLUT_DOWN :
			  glutIdleFunc(self.spin_func)
          if button == GLUT_RIGHT_BUTTON :
		  if state == GLUT_DOWN :
			  glutIdleFunc(None)
	
  def spin_func(self):
	 self.spin = self.spin + 2.0
	 if (self.spin > 360.0):
		self.spin = self.spin - 360.0
	 glutPostRedisplay() 
   
  def lighting(self):
         glEnable(GL_LIGHTING)
         glEnable(GL_LIGHT0)
         LightAmbient = [0.0, 1.0, 0.0, 1.0]
	 LightDiffuse = [1.0, 0.0, 0.0, 1.0]
	 LightPosition = [1.0,1.0, 1.0, 0.0]
	 LightSpot = [-1.0, -1.0 , 0.0]
	 glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, LightSpot)
	 glLightfv(GL_LIGHT0, GL_AMBIENT, LightAmbient)
         glLightfv(GL_LIGHT0, GL_DIFFUSE, LightDiffuse)
         glLightfv(GL_LIGHT0, GL_POSITION, LightPosition)
         #materialAmbDiff = [0.9, 0.1, 1.0, 1.0]
         #glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, materialAmbDiff)
	 materialSpecular = [1.0, 1.0, 1.0, 1.0] # create an array of RGBA values i
         materialShininess = [128.0] # select value between 0-128, 128=shiniest  
	 glMaterialfv(GL_FRONT, GL_SPECULAR, materialSpecular) # set the colour of specular reflection
	 glMaterialfv(GL_FRONT, GL_SHININESS, materialShininess) # set shininess of the material
  

  def plot_func(self):
	  #self.lighting()	  
	  glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	  self.lighting()
	  glColor3f(1.0, 1.0, 1.0)
	  #glMatrixMode(GL_PROJECTION)
	  #glMatrixMode(GL_MODELVIEW)
	  #glShadeModel(GL_SMOOTH)
	  glEnable(GL_DEPTH_TEST)
	  #glMatrixMode(GL_MODELVIEW)
	  #gluLookAt(0.0,10.0,10.0,0.0,1.0,0.0,0.0,1.0,0.0)
	  glPushMatrix()
          glRotatef(self.spin, 0.0, 0.5, 1.0)
	  self.rotate_translate()

	  glColor3f(1.0,0.5,0.0)
	  glLineWidth(3.0)
          for x in arange(-self.axrange + 1, self.axrange - 1, 0.5):
                  glBegin(GL_LINE_STRIP)
                  for y in arange(-self.axrange + 1, self.axrange - 1, 0.5):
                          z = sin(x) +  cos(y)
			  if z >= 0 : 
				glColor3f(z, 0.25 * z, 0.125 * z)
			  else :
				glColor3f(0.125 * abs(z), 0.25 * abs(z), abs(z))
			  glVertex3f(x,y,z)
                  glEnd()
			  
	  for y in arange(-self.axrange + 1, self.axrange -1 , 0.5):
		glBegin(GL_LINE_STRIP)
		for x in arange(-self.axrange + 1, self.axrange -1 , 0.5):
			z = sin (x) + cos (y)
			glVertex3f(x, y ,z)

	  	glEnd()
	  #self.lighting()
	  glFlush()
	  glPopMatrix()
	  glutSwapBuffers()
         
  def ChangeSize(self, w, h):
	  nRange = 100.0
	  if h==0 :
		  h = 1
	  glViewport(0, 0, w, h)
	  glMatrixMode(GL_PROJECTION)
	  glLoadIdentity()
	  if w < h :
		  glOrtho(-self.axrange, self.axrange,\
		          -self.axrange * h / w, self.axrange * h / w,\
			  -self.axrange * 1.0, self.axrange * 1.0)
	  else:
		   glOrtho(-self.axrange * w / h, self.axrange * w / h,\
		           -self.axrange, self.axrange,\
		           -self.axrange * 1.0, self.axrange * 1.0)
	  glMatrixMode(GL_MODELVIEW)
	  glLoadIdentity()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DEPTH | GLUT_RGB | GLUT_DOUBLE)
	glutInitWindowSize(600,600)
	glutCreateWindow("Function Plotter")

	draw = Drawing()
	glutReshapeFunc(draw.ChangeSize)
	glutDisplayFunc(draw.plot_func)
	glutMouseFunc(draw.mouse)
	glutKeyboardFunc(draw.keyboard)
	glutMainLoop()

if __name__ == "__main__":
	main()





