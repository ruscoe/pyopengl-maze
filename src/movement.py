import math

class Movement:

    # Distance the camera moves during each step.
    step_distance = 0.05

    def getIntendedPosition(self, camera_rot = 0, camera_x = 0, camera_z = 0):

        position = [camera_x, 0, camera_z];

        position[0] += self.step_distance * math.cos(math.radians(camera_rot + 90))
        position[2] += self.step_distance * math.sin(math.radians(camera_rot + 90))

        return position
