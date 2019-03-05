#checkers01 by Kaylee

from graphics import*

sqSz = 50

chWin = GraphWin("Checker!", sqSz * 10, sqSz * 10)
chWin.setCoords(0, 0, sqSz * 10, sqSz * 10)

sQ = Rectangle(Point(sqSz, sqSz), Point(sqSz * 2, sqSz * 2))
sQ.draw(chWin)


chWin.getMouse()
chWin.close()
                       






