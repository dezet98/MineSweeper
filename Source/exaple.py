import sys

from PyQt5 import QtCore

global time
time = QtCore.QTime(0, 0, 0)


def timerEvent():
    time = time.addSecs(1)
    print(time.toString("hh:mm:ss"))

app = QtCore.QCoreApplication(sys.argv)

timer = QtCore.QTimer()


timer.timeout.connect(timerEvent)
timer.start(1000)

timer.stop()
sys.exit(app.exec_())









'''
from datetime import datetime
import time

if __name__== '__main__':

    initTimeObj = datetime.now()
    nullRef = datetime(initTimeObj.year, initTimeObj.month, initTimeObj.day, 0, 0, 0)

    print("Initial time:")
    print(str(initTimeObj.hour) + ':' + str(initTimeObj.minute) + ':' + str(initTimeObj.second))
    print("")


    while(True):
        time.sleep(1)
        myDiff = datetime.now() - initTimeObj
        myTimeObj = nullRef + myDiff

        print(str(myTimeObj.hour) + ':' + str(myTimeObj.minute) + ':' + str(myTimeObj.second))

        # Now you get a counting as follows:
        # 0:0:1
        # 0:0:2
        # 0:0:3
        # ...
        # 0:0:59
        # 0:1:0
        # 0:1:1
        # 0:1:2
        # ...


'''

