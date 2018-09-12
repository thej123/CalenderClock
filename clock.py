"""
The class Clock is used to simulate a clock.
"""

class Clock(object):

    def __init__(self, hours, minutes, seconds):
        """
        The parameters hours, minutes and seconds have to be integers and much satisfy the following equations:
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """

        self.set_Clock(hours, minutes, seconds)
    
    def set_Clock(self, hours, minutes, seconds):

        if type(hours) == int and 0 <= hours and hours < 24:
            self._hours = hours
        else:
            raise TypeError("Hours have to be integers between 0 and 23!")
        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self._minutes = minutes
        else:
            raise TypeError("Minutes have to be integers between 0 and 60!")
            raise TypeError("Hours have to be integers between 0 and 59!")
        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self._seconds = seconds
        else:
            raise TypeError("Seconds have to be integers between 0 and 59!")
        
    def tick(self):
        """
        This method lets the clock "tick", this means that the internal time will be advanced by one second.
        Examples:
        >>> x = Clock(12,59,59)
        >>> print(x)
        12:59:59
        >>>x.tick()
        >>>print(x)
        13:00:00
        >>>x.tick()
        >>>print(x)
        13:00:01
        """

        if self._seconds == 59:
            self._seconds = 0
            if self._minutes == 59:
                self._minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours += 1
            else:
                self._minutes += 1
        else:
            self._seconds += 1

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours, self._minutes, self._seconds)



if __name__ == "__main__":
    x = Clock(23,59,59)
    print(x)        
    x.tick()
    print(x)
    y = str(x)
    print(type(y))