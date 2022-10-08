import os
try:
    from pynput import keyboard
except:
    print('\033[1m\033[91mPlease install pynput library. You can do it by typing "pip install pynput" in your terminal\033[0m')
    quit()


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


ELEMENTS = 9

# each element is a pole
# in each list the values represent each piece
state = [list(range(1, ELEMENTS+1)), [0]*ELEMENTS, [0]*ELEMENTS]
cursor = 1
pickedPiece = None


def draw():
    cls()

    global state
    global cursor
    global pickedPiece
    global ELEMENTS

    # cursor
    for i in range(len(state)):
        if cursor == i:
            # draw cursor
            print((ELEMENTS+1)*" "+"↓"+ELEMENTS*" ", end="")
        else:
            print(((ELEMENTS*2)+2)*" ", end="")
    print()
    if pickedPiece:
        for i in range(len(state)):
            if cursor == i:
                # draw piece
                spacingStr = (ELEMENTS-pickedPiece)*" "
                pieceStr = (pickedPiece*2+1)*str(pickedPiece)
                print(" "+spacingStr+pieceStr+spacingStr, end="")
            else:
                print(((ELEMENTS*2)+2)*" ", end="")
    print("\n")

    #pieces and poles
    for i in range(ELEMENTS):
        for pole in state:
            piece = pole[i]
            spacingStr = (ELEMENTS-piece)*" "
            pieceStr = piece*str(piece)
            print(" "+spacingStr+pieceStr+"|"+pieceStr+spacingStr, end="")
        print()

    # bases
    for pole in state:
        print(" "+(ELEMENTS*2+1)*"-", end="")
    print()


# actions
def pickPiece():
    global state
    global cursor
    global pickedPiece

    if pickedPiece != None:
        return

    # get the piece on top and its index
    pole = state[cursor]
    i = None
    for j in range(len(pole)):
        if pole[j] > 0:
            i = j
            break

    if i == None:
        # no pieces in this pole
        return

    pickedPiece = state[cursor][i]
    state[cursor][i] = 0
    draw()


def putPiece():
    global state
    global cursor
    global pickedPiece
    global ELEMENTS
    if (pickedPiece != None):
        pole = state[cursor]
        # get the piece on top and its index
        i = ELEMENTS
        for j in range(len(pole)):
            if pole[j] > 0:
                i = j
                break

        if ((i == ELEMENTS) or (pole[i] > pickedPiece)):
            print("\nputting")
            state[cursor][i-1] = pickedPiece
            pickedPiece = None
            draw()


def goLeft():
    global cursor
    if (cursor == 0):
        cursor = len(state)-1
    else:
        cursor -= 1
    draw()


def goRight():
    global cursor
    if (cursor == len(state)-1):
        cursor = 0
    else:
        cursor += 1
    draw()


def onPress(key):
    try:
        if key.name == 'up':
            pickPiece()
        if key.name == 'down':
            putPiece()
        if key.name == 'left':
            goLeft()
        if key.name == 'right':
            goRight()
    except:
        pass


listener = keyboard.Listener(on_press=onPress)
listener.start()
draw()
while True:
    continue
