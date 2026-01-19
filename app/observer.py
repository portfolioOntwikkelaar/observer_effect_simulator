class Observer:
    def __init__(self, sensitivity: float = 1.0):
        self.sensitivity = sensitivity

    def interact(self, state):
        observed = state.observe()
        return observed * self.sensitivity