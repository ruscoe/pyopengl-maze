import random
import numpy

class Generator:

    def generateMap(self, size = 16, rows = 3, columns = 3):

        #
        rows = [0] * size

        #
        first_row = [0] * size

        # An array of sequential numbers from zero to the size of the map.
        # These numbers are sampled to determine which columns and rows
        # will be walls.
        # Example: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        map_range = numpy.arange(size)

        # Determine which columns will be walls.
        # Example: [4, 11, 7]
        sample = random.sample(list(map_range), columns)

        # Mark columns as walls.
        for i in sample:
            first_row[i] = 1

        # Duplicate the first row until the full map size is met.
        for i in range(size):
            rows[i] = first_row

        # TODO: Turn some rows into walls.


        # Hard-coded map for reference.
        #
        # 1 = wall
        # 0 = path
        #
        # rows = [
        # [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        # [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
        # [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        # [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
        # [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        # [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        # [1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        # [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        # [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        # [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        # [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        # [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        # [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        # [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        # [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        # [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
        # ]

        return rows
