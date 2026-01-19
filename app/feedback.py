def feedback_loop(state, signal: float):
    if state.collapsed:
        return
    state.entropy += abs(signal) * 0.01