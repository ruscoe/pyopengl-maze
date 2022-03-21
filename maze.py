from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.collision import Collision
from src.cube import Cube
from src.generator import Generator
from src.plane import Plane
from src.texture import Texture

# Keyboard commands.
KEY_ESCAPE = b'\x1b'
KEY_FORWARD = b'w'
KEY_LEFT = b'a'
KEY_RIGHT = b'd'

window = 0

# Distance the camera moves during each step.
stepdistance = 0.25
# Size of cubes used to create wall segments.
cubesize = 2
# Initial camera position after map is drawn.
camerapos = [-8.0, 0.0, -38.0]
# Initial camera rotation.
camerarot = 0.0

first_run = False

collision = Collision()

map = []

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

        global camerapos, first_run

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
        row_count = 0
        column_count = 0

        wall_x = 0.0
        wall_z = 0.0

        for i in map:

            wall_z = (row_count * (cubesize * -1))

            for j in i:

                # 1 = cube, 0 = empty space.
                if (j == 1):
                    cube.drawcube(walltexture, 1.0)

                    wall_x = (column_count * (cubesize * -1))

                    if (first_run != True):
                        print('Drawing cube at X:', wall_x, 'Z:', wall_z)

                # Move from left to right one cube size.
                glTranslatef(cubesize, 0.0, 0.0)

                column_count += 1

            # Reset position before starting next row, while moving
            # one cube size towards the camera.
            glTranslatef(((cubesize * column_count) * -1), 0.0, cubesize)

            row_count += 1
            # Reset the column count; this is a new row.
            column_count = 0

        glutSwapBuffers()

        if (first_run != True):
            first_run = True

def handleKeypress(*args):

    global camerapos, camerarot

    if args[0] == KEY_ESCAPE:
        sys.exit()

    # Move forward relative to camera rotation.
    if args[0] == KEY_FORWARD:

        print('Camera X:', camerapos[0], 'Z:', camerapos[2])

        # TODO: Is this space occupied by a wall?
        if (collision.testCollision(cubesize, map, camerapos[0], camerapos[2])):
            print('Collision!')

        if (camerarot == 90):
            camerapos[0] -= stepdistance

        elif (camerarot == 180):
            camerapos[2] -= stepdistance

        elif (camerarot == 270):
            camerapos[0] += stepdistance

        else:
            camerapos[2] += stepdistance

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

        global window, ceilingtexture, floortexture, walltexture, map

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(200, 200)

        window = glutCreateWindow('Experimental Maze')

        # Generate map.
        generator = Generator()
        map = generator.generateMap(16)

        # Represents a top-down view of the maze.
        # map = [
        #     [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        #     [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        #     [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        #     [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        #     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        #     [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        #     [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        #     [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        #     [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #     [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        #     [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        #     [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
        # ]

        map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

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
