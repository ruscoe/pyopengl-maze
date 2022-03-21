
class Collision:

    def testCollision(self, cube_size = 0, map = [], x = 0, z = 0):

        wall_x = 0.0
        wall_z = 0.0

        row_count = 0
        column_count = 0

        half_cube_size = (cube_size / 2)

        for i in map:

            wall_z = (row_count * (cube_size * -1))

            for j in i:

                if (j == 0):
                    # Empty space; increment column count and skip over.
                    column_count += 1
                    continue

                wall_x = (column_count * (cube_size * -1))

                # Check for collision on the z axis.
                if (z == wall_z) or ((z > (wall_z - half_cube_size)) and (z < (wall_z + half_cube_size))):
                    # Hit! Check for collision on the x axis.
                    if (x == wall_x) or ((x > (wall_x - half_cube_size)) and (x < (wall_x + half_cube_size))):
                        print('Collided with wall at X:', wall_x, 'Z:', wall_z)
                        return True

                column_count += 1

            row_count += 1
            column_count = 0

        return False
