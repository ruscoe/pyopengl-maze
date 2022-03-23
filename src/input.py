
class Input:

    # Keyboard commands.
    KEY_ESCAPE = b'\x1b' # Esc
    KEY_FORWARD = b'w'   # W
    KEY_LEFT = b'a'      # A
    KEY_RIGHT = b'd'     # D

    KEY_STATE_ESCAPE = 0  # Esc
    KEY_STATE_FORWARD = 1 # W
    KEY_STATE_LEFT = 2    # A
    KEY_STATE_RIGHT = 3   # D

    key_states = [0] * 4

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

        if key == self.KEY_LEFT:
            self.key_states[self.KEY_STATE_LEFT] = state

        if key == self.KEY_RIGHT:
            self.key_states[self.KEY_STATE_RIGHT] = state
