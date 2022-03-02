'''
Richard Feng
ICS3U - February 14, 2022
Task: Create an adventure game that allows the user to traverse through imaginary land such that at every location, the respective function gets called. 
Name of the setting: Transported to the world of VALORANT
File: agents.py is initializing parent class attributes
'''

# initialization for the agent/character Jett
# this includes keeping track of all her abilities as in how much she has and if she has an adequate amount of bladestorm points to utilize her ultimate ability
class jett:
    def __init__(self, cloudburst, updraft, dash, bladestorm_points):
        self.cloudburst = cloudburst
        self.updraft = updraft
        self.dash = dash
        self.bladestorm_points = bladestorm_points

# initialization for the agent/character Astra
# this includes keeping track of all her abilities as in how much she has and if she has an adequate amount of cosmic divide points to utilize her ultimate ability
class astra:
    def __init__(self, stars, gravity_well, nova_pulse, nebula, cosmic_divide_points):
        self.stars = stars
        self.gravity_well = gravity_well
        self.nova_pulse = nova_pulse
        self.nebula = nebula
        self.cosmic_divide = cosmic_divide
