from fastapi import APIRouter
from app.state import SystemState
from app.observer import Observer
from app.feedback import feedback_loop

router =APIRouter()

state = SystemState()
system_observer = Observer()

@router.get("/observe")
def observe():
    signal = system_observer.interact(state)

    if signal is None:
        return {
            "status": "collapsed",
            "message": "System has irreversibly collapsed"
        }
    feedback_loop(state, signal)
    return {
        "observed_signal": signal,
        "entropy": state.entropy
    }

@router.get("/state")
def get_state():
    return state.raw()