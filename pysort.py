# -*- coding: utf-8 -*
import math
import random
import os
import sys
import time
import io
import traceback

llettres="0123456789abcdefghijklmnopqrstuvwxyz"

continuer=True

def sort(string):
    exe=True
    if type(string)!=str:
        
        print("""AttributeError in function sort : argument must be string""")
        exe=False


    if exe==True:
        chronodeb=time.time ()
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

        chronof=time.time ()
    
        return(output,chronof-chronodeb)

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
