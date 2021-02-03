from importlib import import_module

# The following code returns the module for a state


def get_state(state_code=False):
    if state_code:
        court_module = import_module(f'.states.{state_code}', package=__package__)
        return court_module
    else:
        return False
