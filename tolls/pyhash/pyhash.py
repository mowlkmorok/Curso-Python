#!/bin/python3
import hashlib,sys



try:

    

    if sys.argv[1] == "" :
        print("SSS")

    datafile = sys.argv[1]

    str_encrypted = sys.argv[2]


    fille = open(datafile, "r")

    with open(datafile) as file1:
        if str_encrypted in file1.readlines():
            print(fille.readlines())



    for lines, line_result in enumerate(fille):
        if str_encrypted in fille.read():

            pass1 = str(line_result).split(" ", 1)
            
            print("")
            print("+++++++++++++++++++++++++++++++++++")

            print("Founded [OK] !")

            print("+++++++++++++++++++++++++++++++++++")
            print("Decrypted: ", pass1[0])
            print("Hash: ", pass1[1])




except err:

    print(err)

