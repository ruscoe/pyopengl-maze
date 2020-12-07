from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import open

class Cube:

    def drawcube(self, texture_id = None):

        if texture_id is not None:
            glEnable(GL_TEXTURE_2D)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

            glBindTexture(GL_TEXTURE_2D, texture_id)

        glBegin(GL_QUADS)

        # Textured cube.
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0);
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0);
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0);
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
        glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0);
        glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0);
        glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0);
        glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0);
        glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0);
        glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0);
        glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0);

        # Colored cube.
        #
        # glColor3f(1.0, 0.5, 0.0)
        # glVertex3f( 1.0, 1.0, 1.0)
        # glVertex3f(-1.0, 1.0, 1.0)
        # glVertex3f(-1.0,-1.0, 1.0)
        # glVertex3f( 1.0,-1.0, 1.0)
        #
        # glColor3f(1.0, 0.0, 0.5)
        # glVertex3f( 1.0,-1.0,-1.0)
        # glVertex3f(-1.0,-1.0,-1.0)
        # glVertex3f(-1.0, 1.0,-1.0)
        # glVertex3f( 1.0, 1.0,-1.0)
        #
        # glColor3f(0.0, 1.0, 0.5)
        # glVertex3f(-1.0, 1.0, 1.0)
        # glVertex3f(-1.0, 1.0,-1.0)
        # glVertex3f(-1.0,-1.0,-1.0)
        # glVertex3f(-1.0,-1.0, 1.0)
        #
        # glColor3f(0.5, 0.0, 1.0)
        # glVertex3f(1.0, 1.0,-1.0)
        # glVertex3f(1.0, 1.0, 1.0)
        # glVertex3f(1.0,-1.0, 1.0)
        # glVertex3f(1.0,-1.0,-1.0)

        glEnd()
