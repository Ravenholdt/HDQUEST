class Character(object):
    name = ""

    # Background
    background = {}
    family = {}

    # Stats
    attributes = {}
    personality = {}

    # Skills
    language_spoken = {}
    language_written = {}

    skills = {}
    skills['valfri'] = 0
    skills['yrke'] = 0

    # Equipment
    equipment = {}
    coins = {}


    # The class "constructor" - It's actually an initializer 
    def __init__(self, name):
        self.name = name

def new_character(name = "Gen"):
    character = Character(name)
    print 'Character created.'
    return character