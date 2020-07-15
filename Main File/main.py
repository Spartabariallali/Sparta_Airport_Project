from welcome_interface import Welcome_interface
"""
This file will only contain the run applications, we always run code from this file

Consider creating some form of function with checks the connection
Potentially create an exception to stop the red errors breaking the code
"""


def run_it_all():
    obj1 = Welcome_interface()
    obj1.user_interaction_passengers()

run_it_all()
