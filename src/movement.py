
class Movement:

    # Distance the camera moves during each step.
    step_distance = 0.25
    # The angle in degrees the camera rotates each turn.
    rotate_angle = 5;

    def getIntendedPosition(self, camera_rot = 0, camera_x = 0, camera_z = 0):

        position = [camera_x, 0, camera_z];

        if (camera_rot == 90):
            #intended_x -= stepdistance
            position[0] -= self.step_distance

        elif (camera_rot == 180):
            #intended_z -= stepdistance
            position[2] -= self.step_distance

        elif (camera_rot == 270):
            #intended_x += stepdistance
            position[0] += self.step_distance

        else:
            #intended_z += stepdistance
            position[2] += self.step_distance

        return position
