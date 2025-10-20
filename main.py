from board import rgbled_board, motor

rgbled_board.clear()
motor.turn_right(50, 1)
rgbled_board.set_color(0, '#000000')
rgbled_board.show()

while True:
    pass
