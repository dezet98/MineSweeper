def initialize():
    global game_over
    game_over = False

    global number_of_no_bomb
    number_of_no_bomb = 0

    global number_of_bomb
    number_of_bomb = 0

    global xyzzy    # this value is need in keyPressEvent to check clicked a sequence: xyzzy
    xyzzy = 0

    global game_pause
    game_pause = False

    global time
    time = '00:00:00'

