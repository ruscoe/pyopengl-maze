from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Cube:

    @staticmethod
    def drawcube():
        glBegin(GL_QUADS)

        glColor3f(1.0, 0.5, 0.0)
        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glVertex3f( 1.0,-1.0, 1.0)

        glColor3f(1.0, 0.0, 0.5)
        glVertex3f( 1.0,-1.0,-1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f( 1.0, 1.0,-1.0)

        glColor3f(0.0, 1.0, 0.5)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f(-1.0,-1.0, 1.0)

        glColor3f(0.5, 0.0, 1.0)
        glVertex3f(1.0, 1.0,-1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0,-1.0, 1.0)
        glVertex3f(1.0,-1.0,-1.0)

        glEnd()
