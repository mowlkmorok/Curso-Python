#!/bin/usr/python3

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        print("                ____")
        print("Don't divibe by zero")
        print("                ----")

def main():
    while True:    
        tocall() 
        n1 = float(input("Set 1° Number:"))
        n2 = float(input("Set 2° Number:"))

        print("""
        [1] - Add
        [2] - Subtraction
        [3] - Multiplication
        [4] - Division
        """)
        op = input("Set Options:\n>> ")

        print("#####################################")

        dic_options = {
                '1': add,
                '2': sub,
                '3': mult,
                '4': div
                }

        if options in dic_options.keys():
            dic[op](n1, n2)
        else:
            print("Invalid Option!")

def tocall():
    exi = input("Enter in Caculater 1-Exit 2-Continue\n>")
    if exi == '1':
        exit()
    elif exi == '2':
        pass
    else:
        print("Invalid Option")

if __name__ == '__main__':
    main()

exit()

text = """ Ola João como vai?; Por aqui esta bem Maria e por ai; Maria diz: vai bem João graças a Deus,
João diz: E os pestinhas amados dos seus filhos como estão, eles aprontavam muitissimo aqui nas minhas terras viu, comia manga, corria atrás dos cavaos, com maior fuzue. joão
>Maria diz: Nossa aqueles meus filhos era seu, né seu safado.
"""
print(text)

print("##########################################################")

cont_joao = 0

ww = input("Enter the word: ")
word = ww.upper()


for palavra in text.split():
    if palavra.upper() == word:
        cont_joao += 1

