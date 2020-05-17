#!/bin/usr/python3

lista = []


def new_register(lista):
    dic = {}
    dic['name'] = input("Name: ")
    dic['age'] = int(input("Age: "))
    dic['sexop'] = input("Sex option: ")
    dic['uf'] = input("UF: ")
    lista.append(dic)
    print('>Register successfully added<\n\n\n')
    

def register_show(lista):
    for datas in lista:
        print('___________________________________________')
        print(f'''                          
               Name:       {datas['name']}
               Age:        {datas['age']}
               Sex Option: {datas['sexop']}
               UF:         {datas['uf']}
               
               ''')


def major(lista):
    for mage in lista:
        if mage['age'] < 18:
            print("________________________________________")
            print('Minor: ', mage['name'])
            print('')

def uf_filter(lista):
    state = input('Search UF: ')

    for data in lista:
        if data['uf'].upper() == state.upper():
            print("___________________________________________")
            print('Name: ', data['name'])
            

def main():
    while True:
        options = {
                '1':new_register,
                '2':register_show,
                '3':uf_filter,
                '4':major,
                '5':exit
                } 


        print('Set options:\n1-New register\n2-Register show\n3-UFfilter\n4-Minor Search\n5-Exit\n')
        option = input('Set Option:\n> ')

        if option in options.keys():
            print(options[option](lista))

        else:
            print('Invalid Option!')


if __name__ == '__main__':
    main()
