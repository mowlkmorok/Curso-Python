lista = []


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def exi():
    exi = input("1-Continue\n2-Exit\n")
    if exi == '1':
        pass
    elif exi == '2':
        exit('Bye!...')


def exe():
    exit()


def ss():
    pass


def main():
    while True:
        xxe = {
            '1': ss,
            '2': exe
        }
        op = input("1-Continue\n2-Exit\n>")
        if op in xxe.keys():
            xxe[op]()
        else:
            print('Invalid Option!')
            main()

        print('Set:\n')
        n1 = float(input('N1:'))
        n2 = float(input('N2:'))
        options = {
            '1': add,
            '2': sub,
            '3': mult,
            '4': div,
            '5': exit
        }
        print('_________________________________________')
        print('1- Add\n2-Subtract\n3-Multiplication\n4-Division\n5-Exit\n')
        option = input("Set Options\n>")
        if option in options.keys():
            print(options[option](n1, n2))


if __name__ == '__main__':
    main()
exit()