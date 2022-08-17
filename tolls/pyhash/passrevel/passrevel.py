#!/bin/python3

import crypt
import sys


try:

    salt = sys.argv[1]
    hash1 = sys.argv[2]

    pASSFILE = sys.argv[3]



    with open(pASSFILE) as file1:

        print("+++++++++++++HASHES COMPARING+++++++++")
        for lines in file1.readlines():

            #=========STRING PARSING AJUST
            str_parsed = lines.replace("\n", ":").replace(":","")
           
            crypted = crypt.crypt(str_parsed,str(salt))

            #=========HASHES COMPARING
            
            if crypted == str(salt+"."+hash1):
                print("Decryted string: ", str_parsed)
                exit

            elif crypted == salt+hash1:
                print("Perherps: ", str_parsed)
                exit
            elif crypted == salt+"$"+hash1:
                print( "Perherps: ", str_parsed)
                exit

            else:
                print("NOT FOUNDED [!]")
                exit




except err:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Error [!]")


    print("Syntax expemple:\n")
    print("[PROGRAM] [SALT] [HASH] [HASH-WORDLIST]")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    print(err)
