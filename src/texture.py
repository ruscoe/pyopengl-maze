from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL.Image import open
import numpy

class Texture:

    def loadImage(self, filename):
        try:
            image = open(filename)
        except IOError as ex:
            print('IOError: failed to open texture file')
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return -1

        print('Opened image file: size =', image.size, 'format =', image.format)
        imageData = numpy.array(list(image.getdata()), numpy.uint8)

        textureID = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 4)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_BASE_LEVEL, 0)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAX_LEVEL, 0)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.size[0], image.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, imageData)

        image.close()

        return textureID
