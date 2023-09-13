#!/usr/bin/python3


""" This module implements a list inheritor """


class MyList(list):
    """
    Class that inherits list
    """

    def print_sorted(self):
        """
        Prints sorted list
        """
        myL = self.copy()
        myL.sort()
        print(myL)
