from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from src.collision import Collision
from src.cube import Cube
from src.generator import Generator
from src.input import Input
from src.map import Map
from src.movement import Movement
from src.plane import Plane
from src.sprite import Sprite
from src.texture import Texture
import argparse

window = 0

# Size of cubes used to create wall segments.
cube_size = 2
# Space around cubes to extend hitbox (prevents peeking through walls).
collision_padding = 0.5
# Initial camera position after map is drawn.
camera_pos = [-8.0, 0.0, -38.0]
# camerapos = [0.0, 0.0, 0.0]
# Initial camera rotation.
camera_rot = 0.0
# The angle in degrees the camera rotates each turn.
rotate_angle = 1

collision = Collision()
input = Input()
movement = Movement()

map = []

# Loaded textures.
ceiling_texture = None
floor_texture = None
wall_textures = []
object_textures = []
door_textures = []
objects = []

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

    global camera_pos

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    cube = Cube()
    plane = Plane()
    sprite = Sprite()

    # Set up the current maze view.
    # Reset position to zero, rotate around y-axis, restore position.
    glTranslatef(0.0, 0.0, 0.0)
    glRotatef(camera_rot, 0.0, 1.0, 0.0)
    glTranslatef(camera_pos[0], camera_pos[1], camera_pos[2])

    # Draw floor.
    glPushMatrix()
    glTranslatef(0.0, -2.0, 0.0)
    glScalef(30.0, 1.0, 30.0)
    plane.drawplane(floor_texture, 10.0)
    glPopMatrix()

    # Draw ceiling.
    glPushMatrix()
    glTranslatef(0.0, 2.0, 0.0)
    glRotatef(180.0, 0.0, 0.0, 1.0)
    glScalef(30.0, 1.0, 30.0)
    plane.drawplane(ceiling_texture, 10.0)
    glPopMatrix()

    # Build the maze like a printer; back to front, left to right.
    row_count = 0
    column_count = 0

    objects = []

    for i in map:

        for j in i:

            # 0 = empty space.
            # 1 - 9 = wall.
            if ((j > 0) and (j < 10)):
                # Wall textures are zero-indexed, so subtract 1 from wall ID.
                cube.drawcube(wall_textures[int(j) - 1], 1.0)

            if ((j > 9) and (j < 20)):
                objects.append([column_count, row_count, j])

            # Move from left to right one cube size.
            glTranslatef(cube_size, 0.0, 0.0)

            column_count += 1

        # Reset position before starting next row, while moving
        # one cube size towards the camera.
        glTranslatef(((cube_size * column_count) * -1), 0.0, cube_size)

        row_count += 1
        # Reset the column count; this is a new row.
        column_count = 0

    # Reset to start of map.
    glTranslatef(0.0, 0.0, ((row_count * cube_size) * -1))

    # Draw object sprites.
    for object in objects:
        glPushMatrix()
        glTranslatef((object[0] * cube_size), 0.0, (object[1] * cube_size))
        glRotatef(90.0, 1.0, 0.0, 0.0)
        glRotatef(camera_rot, 0.0, 0.0, 1.0)
        glScalef(1.0, 0.0, 1.0)
        # Object textures are zero-indexed, so subtract 10 from object ID.
        sprite.drawSprite(object_textures[int(object[2]) - 10])
        glPopMatrix()

    glutSwapBuffers()

    handleInput()

def handleInput():

    global input, camera_pos, camera_rot

    if input.isKeyDown(Input.KEY_STATE_ESCAPE):
        sys.exit()

    if input.isKeyDown(Input.KEY_STATE_LEFT):
        camera_rot -= rotate_angle

    if input.isKeyDown(Input.KEY_STATE_RIGHT):
        camera_rot += rotate_angle

    intended_pos = [camera_pos[0], 0, camera_pos[2]]

    if input.isKeyDown(Input.KEY_STATE_FORWARD) or input.isKeyDown(Input.KEY_STATE_BACK):
        modifier = 1 if input.isKeyDown(Input.KEY_STATE_FORWARD) else -1
        intended_pos = movement.getIntendedPosition(camera_rot, camera_pos[0], camera_pos[2], 90, modifier)

    if input.isKeyDown(Input.KEY_STATE_LEFT_STRAFE) or input.isKeyDown(Input.KEY_STATE_RIGHT_STRAFE):
        modifier = 1 if input.isKeyDown(Input.KEY_STATE_LEFT_STRAFE) else -1
        intended_pos = movement.getIntendedPosition(camera_rot, camera_pos[0], camera_pos[2], 0, modifier)

    intended_x = intended_pos[0]
    intended_z = intended_pos[2]

    # Detect collision with walls.
    if (collision.testCollision(cube_size, map, intended_x, intended_z, collision_padding)):
        # print('Collision at X:', intended_x, 'Z:', intended_z)

        # If it's possible to keep the user moving by sliding along the wall, do so.
        slide_time = False
        if (collision.testCollision(cube_size, map, intended_x, camera_pos[2], collision_padding) == False):
            intended_z = camera_pos[2]
            slide_time = True
        elif (collision.testCollision(cube_size, map, camera_pos[0], intended_z, collision_padding) == False):
            intended_x = camera_pos[0]
            slide_time = True

        if (slide_time):
            # Slide the camera along the wall.
            camera_pos[0] = intended_x
            camera_pos[2] = intended_z
    else:
        # Move the camera to the user's intended position.
        camera_pos[0] = intended_x
        camera_pos[2] = intended_z

def main():

    global window, ceiling_texture, floor_texture, object_textures, map

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1024, 768)
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow('Experimental Maze')

    # Get map name from arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--map', help='The map to load.')
    args = parser.parse_args()

    if (args.map != None):
        map = Map.loadMap(args.map)
    else:
        # Generate random map if no map is specified.
        generator = Generator()
        map = generator.generateMap(16)

    # Load textures.
    texture = Texture()

    ceiling_texture = texture.loadImage('tex/ceiling.png')
    floor_texture = texture.loadImage('tex/floor.png')

    wall_textures.append(texture.loadImage('tex/wall/01.png'))
    wall_textures.append(texture.loadImage('tex/wall/02.png'))

    object_textures.append(texture.loadImage('tex/object/orb.png'))

    door_textures.append(texture.loadImage('tex/door/01.png'))

    glutIgnoreKeyRepeat(1)
    glutKeyboardFunc(input.registerKeyDown)
    glutKeyboardUpFunc(input.registerKeyUp)

    glutDisplayFunc(drawScene)
    glutIdleFunc(drawScene)
    initGL(1024, 768)
    glutMainLoop()

if __name__ == "__main__":

    main()
