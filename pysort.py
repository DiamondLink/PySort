# -*- coding: utf-8 -*
#By DiamondLink
#TEST
import math
import random
import os
import sys
import time
import io
import traceback

stringSortingList = "0123456789abcdefghijklmnopqrstuvwxyz"
listStartSortingList = list("abcdefghijklmnopqrstuvwxyz")

def sort(toSort):
    if type(toSort) != str and type(toSort) != list:
        raise AttributeError("Specified object to sort must be string or list")

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
            listSortingList = listStartSortingList
            for i in range(min, max+1):
                listSortingList.append(str(i))

            sortedList = []
            for el in listSortingList:
                print(el)
                for element in toSort:
                    print(element)
                    if el == str(element).lower():
                        sortedList.append(element)

        return sortedList

    elif type(toSort) == str:
        listedeux = []
        i = 0

        sortedString = ""

        for element in toSort:
            i += 1

        list_str = [""]*i
        i = 0

        for element in stringSortingList:
            for el in toSort:
                if el.lower() == element:
                    sortedString += el

        return sortedList


if __name__ == "__main__":

    while continuer == True:
        continuer = False
        print("\n")
        string = input("Enter string to sort out : ")
        for element in string:

            if element not in llettres:
                print("\n")
                print("Only letter and number sorting is available")
                print("\n")
                continuer = True
                break

    sort(string)
