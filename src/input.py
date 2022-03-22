
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
        key_state = 0

        if key == self.KEY_ESCAPE:
            key_state = self.KEY_STATE_ESCAPE

        if key == self.KEY_FORWARD:
            key_state = self.KEY_STATE_FORWARD

        if key == self.KEY_LEFT:
            key_state = self.KEY_STATE_LEFT

        if key == self.KEY_RIGHT:
            key_state = self.KEY_STATE_RIGHT

        self.key_states[key_state] = state
