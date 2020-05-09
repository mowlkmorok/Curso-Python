print("""
#############################
#########CALCULATER##########
#############################
""")

print("Push 1 for enter or 2 for exit")
ent = int(input("1 or 2:\n> "))

if ent == 1:
    ma(ent)
elif ent == 2:
   exit()
else:
    print("Invalit argument")

def ma(ent):
    print("Your heady?")
    print("#"*20)

    n1 = bool(input("N°1:"))
    n2 = bool(input("N°1:"))
    op = int(input("Set option + - * /"))

    print("""
    [1]-Add
    [2]-Sub
    [3]-Mult
    [4]-Div
    """)


    while 1:
    	if op == 1:
            print(n1 + n2)
    	elif op == 2:
            print(n1 - n2)
    	elif op == 3:
            print(n1 * n2)
        if not n2 == 0:
            print("0 NO divised!")
            if op == 4:
                print(n1 / n2)
	else:
	    print("Invalid atgument[!]")

exit("End Cod..")
