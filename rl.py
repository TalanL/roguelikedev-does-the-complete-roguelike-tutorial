from bearlibterminal import terminal

terminal.open()
terminal.printf(1, 1, "Hello, /r/roguelikedev!")
terminal.refresh()

while terminal.read() != terminal.TK_CLOSE:
    pass

terminal.close()
