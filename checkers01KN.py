#checkers01 by Kaylee

from graphics import*

def draw_sq(sX, sY, size, color, win):
    square = Rectangle(Point(sX, sY), Point(sX + size, sY + size))
    square.setFill(color)
    square.draw(win)

sqSz = 50

chWin = GraphWin("Checker!", sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)

sQ = Rectangle(Point(sqSz, sqSz), Point(sqSz * 2, sqSz * 2))
sQ.setFill("red")
sQ.draw(chWin)


chWin.getMouse()
chWin.close()
                       






