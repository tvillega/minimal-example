import time

def countdown():
    """ Counts from 4 to 0

    This functions is a countdown that starts at 5 and ends at 0
    """

    for i in range(0,5): print(4-i) ; time.sleep(0.5)

countdown()
