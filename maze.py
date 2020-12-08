from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.cube import Cube
from src.plane import Plane
from src.texture import Texture

# Keyboard commands.
KEY_ESCAPE = b'\x1b'
KEY_FORWARD = b'w'
KEY_LEFT = b'a'
KEY_RIGHT = b'd'

window = 0
cubesize = 2
# Initial camera position after map is drawn.
camerapos = [-8.0, 0.0, -38.0]
# Initial camera rotation.
camerarot = 0.0

# Loaded textures.
ceilingtexture = None
floortexture = None
walltexture = None

def initGL(Width, Height):

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

def drawScene():

        # Represents a top-down view of the maze.
        # 1 = wall
        # 0 = path
        # This could be built procedurally; hard-coded for now.
        map = [
            [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
        ]

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()

        cube = Cube()
        plane = Plane()

        # Set up the current maze view.
        # Reset position to zero, rotate around y-axis, restore position.
        glTranslatef(0.0, 0.0, 0.0)
        glRotatef(camerarot, 0.0, 1.0, 0.0)
        glTranslatef(camerapos[0], camerapos[1], camerapos[2])

        # Draw floor.
        glPushMatrix()
        glTranslatef(0.0, -2.0, 0.0)
        glScalef(30.0, 1.0, 30.0)
        plane.drawplane(floortexture, 40.0)
        glPopMatrix()

        # Draw ceiling.
        glPushMatrix()
        glTranslatef(0.0, 2.0, 0.0)
        glRotatef(180.0, 0.0, 0.0, 1.0)
        glScalef(30.0, 1.0, 30.0)
        plane.drawplane(ceilingtexture, 50.0)
        glPopMatrix()

        # Build the maze like a printer; back to front, left to right.
        columncount = 0

        for i in map:

            for j in i:

                # 1 = cube, 0 = empty space.
                if (j == 1):
                    cube.drawcube(walltexture, 1.0)

                # Move from left to right one cube size.
                glTranslatef(cubesize, 0.0, 0.0)

                columncount += 1

            # Reset position before starting next row, while moving
            # one cube size towards the camera.
            glTranslatef(((cubesize * columncount) * -1), 0.0, cubesize)
            # Reset the column count; this is a new row.
            columncount = 0

        glutSwapBuffers()

def handleKeypress(*args):

    global camerapos, camerarot

    if args[0] == KEY_ESCAPE:
        sys.exit()

    # Move forward relative to camera rotation.
    if args[0] == KEY_FORWARD:

        if (camerarot == 90):
            camerapos[0] -= cubesize

        elif (camerarot == 180):
            camerapos[2] -= cubesize

        elif (camerarot == 270):
            camerapos[0] += cubesize

        else:
            camerapos[2] += cubesize

    if args[0] == KEY_LEFT:
        camerarot -= 90.0

    if args[0] == KEY_RIGHT:
        camerarot += 90.0

    # Enforce minimum and maximum rotation.
    if (camerarot < 0):
        camerarot = 270

    if (camerarot > 270):
        camerarot = 0

def main():

        global window, ceilingtexture, floortexture, walltexture

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(200, 200)

        window = glutCreateWindow('Experimental Maze')

        # Load texture.
        texture = Texture()
        ceilingtexture = texture.loadImage('tex/ceiling.bmp')
        floortexture = texture.loadImage('tex/floor.bmp')
        walltexture = texture.loadImage('tex/wall.bmp')

        glutKeyboardFunc(handleKeypress)

        glutDisplayFunc(drawScene)
        glutIdleFunc(drawScene)
        initGL(640, 480)
        glutMainLoop()

if __name__ == "__main__":

        main()
