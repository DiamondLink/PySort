# -*- coding: utf-8 -*
#By DiamondLink
import math
import random
import os
import sys
import time
import io
import traceback
import time

def funcExeAndTime(function, *args, **kwargs):
    """Execute a fonction and get the execution time, usefull for testing the efficiency and a sorting algotithme"""
    start = time.time()
    function(*args, **kwargs)
    return(time.time() - start)

def sort(toSort,onlySortRightTypeOfElements = False):  #Only type means that string will be ignored when sotring an array and int and float will be ignored when sorting a string 
    if type(toSort) != str and type(toSort) != list:
        raise AttributeError("Specified object to sort must be string or list")

    if type(onlySortRightTypeOfElements) != bool:
        raise AttributeError("onlySortRightTypeOfElements must be a boolean")

    BaseSortingList = "abcdefghijklmnopqrstuvwxyz"

    if type(toSort) == list:
        max = None
        for el in toSort:
            if max == None:
                max = el
                min = el
            else:
                try:
                    if max < el:
                        max = el
                    if min > el:
                        min = el
                except TypeError:
                    pass
        
        if onlySortRightTypeOfElements == False:    #SLOWER
            listSortingList = list(BaseSortingList)
        else:                                       #FASTER
            listSortingList = list()
        for i in range(min, max+1):
            listSortingList.append(str(i))

        Sorted = []
        for el in listSortingList:
            for element in toSort:
                if el == str(element).lower():
                    Sorted.append(element)

    elif type(toSort) == str:
        Sorted = ""

        if onlySortRightTypeOfElements == False:    #SLOWER
            BaseSortingList = "0123456789" + BaseSortingList

        for element in BaseSortingList:
            for el in toSort:
                if el.lower() == element:
                    Sorted += el

    return Sorted

def main():
    import sys
    import os

    try:
        from colorama import Fore
    except:
        raise ImportError("Can't import colorama ! Make sure it's installed")

    if sys.version_info[0] < 3:
        raise EnvironmentError("Must be using Python 3")

    print("\n{}Pysort : most efficient sorting algorithme ever ! (actually it's not the fastest but it doesn't matter)\n\n{}Chose sorting type :\n1 : String sorting\n2 : List / Array sorting\n".format(Fore.GREEN,Fore.RESET))

    typeOf = input(">> ")
    print("{}Note that special caracteres will be ignored{}".format(Fore.YELLOW,Fore.RESET))
    elementToSort = input("Input element to sort [Array elements must be separated by a comma] : ")

    print("{}Note that special caracteres will be ignored{}".format(Fore.YELLOW,Fore.RESET))

    if typeOf == "2":
        elementToSort = elementToSort.split(",")
        for i in range(len(elementToSort)):
            try:
                elementToSort[i] = int(elementToSort[i])
            except:
                pass

    elif typeOf != "1":
        print("{}You must chose a valid option (1 or 2){}".format(Fore.RED,Fore.RESET))
        sys.exit(0)

    return(sort(elementToSort))

if __name__=="__main__":
    print(main())
