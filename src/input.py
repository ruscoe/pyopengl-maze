
class Input:

    # Keyboard commands.
    KEY_ESCAPE = b'\x1b'    # Esc
    KEY_FORWARD = b'w'      # W
    KEY_BACK = b's'         # S
    KEY_LEFT = b'a'         # A
    KEY_RIGHT = b'd'        # D
    KEY_LEFT_STRAFE = b','  # ,
    KEY_RIGHT_STRAFE = b'.' # .

    KEY_STATE_ESCAPE = 0
    KEY_STATE_FORWARD = 1
    KEY_STATE_BACK = 2
    KEY_STATE_LEFT = 3
    KEY_STATE_RIGHT = 4
    KEY_STATE_LEFT_STRAFE = 5
    KEY_STATE_RIGHT_STRAFE = 6

    key_states = [0] * 7

    def isKeyDown(self, key_state):
        return (self.key_states[key_state] == 1)

    def registerKeyDown(self, key, x, y):
        self.setKeyState(key, 1)

    def registerKeyUp(self, key, x, y):
        self.setKeyState(key, 0)

    def setKeyState(self, key, state):
        if key == self.KEY_ESCAPE:
            self.key_states[self.KEY_STATE_ESCAPE] = state

        if key == self.KEY_FORWARD:
            self.key_states[self.KEY_STATE_FORWARD] = state

        if key == self.KEY_BACK:
            self.key_states[self.KEY_STATE_BACK] = state

        if key == self.KEY_LEFT:
            self.key_states[self.KEY_STATE_LEFT] = state

        if key == self.KEY_RIGHT:
            self.key_states[self.KEY_STATE_RIGHT] = state

        if key == self.KEY_LEFT_STRAFE:
            self.key_states[self.KEY_STATE_LEFT_STRAFE] = state

        if key == self.KEY_RIGHT_STRAFE:
            self.key_states[self.KEY_STATE_RIGHT_STRAFE] = state
