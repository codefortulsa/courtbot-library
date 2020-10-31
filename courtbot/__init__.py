import os

from importlib import import_module

# The following code add states to the courbot object
# to make them available like `courtbot.OK`

def get_state(state_code=False):
    court_module = import_module(f'.states.{state_code}', package=__package__)
    return court_module
