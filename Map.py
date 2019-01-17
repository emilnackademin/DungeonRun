import roomClass
mapcord = []
curx = 0
cury = 0
prevroom = []
demomap = []
sizex = 0
sizey = 0
prevy = 0
prevx = 0


# Mapsize creator
def mapsize(x, y):
    for r in range(x):
        for k in range(y):
            demomap.append([r, k])
            room = roomClass.Room(r, k)
            mapcord.append(room)
    global sizex
    global sizey
    sizex = x
    sizey = y

def map_choice():
    diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
    if diffpick == '1':
        mapsize(4, 4)
    elif diffpick == '2':
        mapsize(5, 5)
    elif diffpick == '3':
        mapsize(8, 8)


# Set corner coodinates
def set_coordninates():
    ne = 0, sizey-1
    sw = sizex-1, 0
    se = sizex-1, sizey-1


# Start room selection
def start_room():
    startroom = input('Were would you like to start?\n[1] Northwest\n[2] Northeast\n[3] Southwest\n[4] Southeast\n')
    if startroom == '1':
        curx = 0
        cury = 0
    elif startroom == '2':
        curx = sizex - 1
        cury = 0
    elif startroom == '3':
        curx = 0
        cury = sizey-1
    elif startroom == '4':
        curx = sizex - 1
        cury = sizey - 1

    print(cury, curx)

# Choose direction
def choose_direction():
    while True:
        direction = input("Choose direction\n[W] to go north\n[A] to go west\n[S] to go south\n[D] to go east\n").lower()
        if direction == 'w':
            prevx = curx
            prevy = cury

            for newroom in mapcord:
                if newroom.gety() == (cury - 1) and newroom.getx() == curx:
                    cury = (newroom.gety())
                    break
            if cury == prevy:
                print("You search the wall for a door but are unable to find one.")
                continue

        elif direction == 's':
            prevx = curx
            prevy = cury

            for newroom in mapcord:
                if newroom.gety() == (cury + 1) and newroom.getx() == curx:
                    cury = (newroom.gety())
                    break
            if cury == prevy:
                print("You search the wall for a door but are unable to find one.")
                continue

        elif direction == 'a':
            prevx = curx
            prevy = cury

            for newroom in mapcord:
                if newroom.getx() == (curx - 1) and newroom.gety() == cury:
                    curx = (newroom.getx())
                    break
            if curx == prevx:
                print("You search the wall for a door but are unable to find one.")
                continue

        elif direction == 'd':
            prevx = curx
            prevy = cury

            for newroom in mapcord:
                if newroom.getx() == (curx + 1) and newroom.gety() == cury:
                    curx = (newroom.getx())
                    break
            if curx == prevx:
                print("You search the wall for a door but are unable to find one.")
                continue

        print(cury, curx)
