from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.collision import Collision
from src.cube import Cube
from src.generator import Generator
from src.input import Input
from src.movement import Movement
from src.plane import Plane
from src.sprite import Sprite
from src.texture import Texture

window = 0

# Size of cubes used to create wall segments.
cubesize = 2
# Space around cubes to extend hitbox (prevents peeking through walls).
collision_padding = 0.5
# Initial camera position after map is drawn.
camerapos = [-8.0, 0.0, -38.0]
# camerapos = [0.0, 0.0, 0.0]
# Initial camera rotation.
camerarot = 0.0
# The angle in degrees the camera rotates each turn.
rotate_angle = 1;

first_run = False

collision = Collision()
input = Input();
movement = Movement();

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
    sprite = Sprite()

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

    # Draw test sprite.
    # glPushMatrix()
    # glTranslatef(0.0, 0.5, -6.0)
    # glRotatef(90.0, 1.0, 0.0, 0.0)
    # glRotatef(camerarot, 0.0, 0.0, 1.0)
    # glScalef(1.0, 0.0, 1.0)
    # sprite.drawSprite(ceilingtexture)
    # glPopMatrix()

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

    handleInput()

    if (first_run != True):
        first_run = True

def handleInput():

    global input, camerapos, camerarot

    if input.isKeyDown(Input.KEY_STATE_ESCAPE):
        sys.exit()

    if input.isKeyDown(Input.KEY_STATE_LEFT):
        camerarot -= rotate_angle

    if input.isKeyDown(Input.KEY_STATE_RIGHT):
        camerarot += rotate_angle

    intended_pos = [camerapos[0], 0, camerapos[2]];

    if input.isKeyDown(Input.KEY_STATE_FORWARD) or input.isKeyDown(Input.KEY_STATE_BACK):
        modifier = 1 if input.isKeyDown(Input.KEY_STATE_FORWARD) else -1
        intended_pos = movement.getIntendedPosition(camerarot, camerapos[0], camerapos[2], 90, modifier)

    if input.isKeyDown(Input.KEY_STATE_LEFT_STRAFE) or input.isKeyDown(Input.KEY_STATE_RIGHT_STRAFE):
        modifier = 1 if input.isKeyDown(Input.KEY_STATE_LEFT_STRAFE) else -1
        intended_pos = movement.getIntendedPosition(camerarot, camerapos[0], camerapos[2], 0, modifier)

    intended_x = intended_pos[0]
    intended_z = intended_pos[2]

    # Move camera if there are no walls in the way.
    if (collision.testCollision(cubesize, map, intended_x, intended_z, collision_padding)):
        print('Collision at X:', intended_x, 'Z:', intended_z)
    else:
        camerapos[0] = intended_x
        camerapos[2] = intended_z

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

    # Load texture.
    texture = Texture()
    ceilingtexture = texture.loadImage('tex/ceiling.bmp')
    floortexture = texture.loadImage('tex/floor.bmp')
    walltexture = texture.loadImage('tex/wall.bmp')

    glutIgnoreKeyRepeat(1)
    glutKeyboardFunc(input.registerKeyDown)
    glutKeyboardUpFunc(input.registerKeyUp)

    glutDisplayFunc(drawScene)
    glutIdleFunc(drawScene)
    initGL(640, 480)
    glutMainLoop()

if __name__ == "__main__":

    main()
