import math

class Movement:

    # Distance the camera moves during each step.
    step_distance = 0.05

    def getIntendedPosition(self, camera_rot = 0, camera_x = 0, camera_z = 0, local_angle = 90, modifier = 1):

        position = [camera_x, 0, camera_z];

        x_offset = self.step_distance * math.cos(math.radians(camera_rot + local_angle))
        z_offset = self.step_distance * math.sin(math.radians(camera_rot + local_angle))

        position[0] += (x_offset * modifier)
        position[2] += (z_offset * modifier)

        return position
