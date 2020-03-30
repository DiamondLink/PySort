# -*- coding: utf-8 -*
import math
import random
import os
import sys
import time
import io
import traceback

stringSortingList="0123456789abcdefghijklmnopqrstuvwxyz"
listStartSortingList=list("abcdefghijklmnopqrstuvwxyz")

def sort(toSort):
    if type(toSort)!=str and type(toSort) != list:
        raise AttributeError("Specified object to sort must be string or list")
        
    if type(toSort)==list:
        max=None
        for el in toSort:
            if max==None:
                max = el
                min = el
            else:
                try:
                    if max < el:
                        max = el
                    if min > el:
                        min = el
                except TypeError:
                    if type(el) != string:
                        raise AttributeError("List to sort must contains int, float or str")
                    
	    listSortingList = listStartSortingList
        for i in range(min,max+1):
	        listSortingList.append(str(i))
            
	    sortedList = []
	    for el in listSortingList:
	        for element in toSort:
	            if el == str(element).lower():
                    sortedList.append(element)
                    
        return sortedList


    elif type(toSort) == str:
        listedeux=[]
        i=0

        for element in string:
                i+=1

        list_str=[""]*i
        i=0

        for element in llettres:
            for el in string:
                if element==el or element.upper()==el:
                    if list_str [i]=="":
                        list_str [i]=el
                    else:
                        i+=1
                        list_str [i]=el
                    i+=1
        for el in string:
            if el not in llettres and el not in llettres.upper():
                listedeux.append(el)
        
        list_str=list_str+listedeux


        output="".join (list_str)

if __name__ == "__main__":


    while continuer==True:
        continuer=False
        print ("\n")
        string=input ("Enter string to sort out : ")
        for element in string:

            if element not in llettres :
                print ("\n")
                print ("Only letter and number sorting is available")
                print ("\n")
                continuer=True
                break

    sort(string)
