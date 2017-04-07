class Player(object):
    name = ""
    socket = 0


    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, conn):
        self.name = name
        self.socket = conn

def new_player(conn, name):
    player = Player(name, conn)
    print 'Player created.'
    return player