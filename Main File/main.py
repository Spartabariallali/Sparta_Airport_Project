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

"""
Thursday evening
Completed Tc and Cs
Fully functional booking database that can link to the Passenger database
Halfway completion of Password encryption
Aircraft Database created
Queries which allow the reassignment of planes to a given destination
"""

"""
Friday Morning TODO:
Implement Password interface into Airplane assignment
Implement Password encryption
Create a connectivity between the number of passengers assigned to a flight and the handling of tickets
Begin allocating Presentation Slides/Code executions
CSV backup file?
"""