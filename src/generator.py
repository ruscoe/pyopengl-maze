import random
import numpy

class Generator:

    def generateMap(self, size = 16, columns_as_walls = 3, rows_as_walls = 3):

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
        sample = random.sample(list(map_range), columns_as_walls)

        # Mark columns as walls.
        for column_id in sample:
            first_row[column_id] = 1

        # Duplicate the first row until the full map size is met.
        for i in range(size):
            rows[i] = first_row.copy()

        # Remove one segment from each column to create pathways.
        for column_id in sample:
            row_to_remove = random.choice(list(map_range))
            rows[row_to_remove][column_id] = 0

        # Determine which rows will be walls.
        # Example: [4, 11, 7]
        sample = random.sample(list(map_range), rows_as_walls)

        # Mark rows as walls.
        for row_id in sample:
            for i in range(size):
                rows[row_id][i] = 1

        # Remove one segment from each row to create pathways.
        for row_id in sample:
            column_to_remove = random.choice(list(map_range))
            rows[row_id][column_to_remove] = 0

        # Uncomment to print map as a grid.
        # for i in range(size):
        #     print(rows[i])

        # Hard-coded map for reference.
        # Uncomment to manually create a map.
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
