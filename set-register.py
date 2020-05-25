def new_reg(reg):
	title_movie = input('Title:')
	genre = input('Movie Genre:')
	year = input('Year:')
	director = input('Direction:')
	
	reg = f'{title_movie};{genre};{year};{director}\n'
	
	with open('movies.csv', 'a+') as arquiv:
		arquiv.write(reg)
	return reg


def searcha(lista):
	
	stitle = input('Seach Title:')
	
	with open('movies.csv', 'r') as data:
		datas = data.readlines()
	for item in datas:
		if stitle in item.split(';'):
		    print('-----------------------------------')
		    print(item.split(';')[0])
		    print(item.split(';')[1])
		    print(item.split(';')[2])
		    print(item.split(';')[3])


def main():
	with open('movies.csv', 'w') as arq:
		cab = 'Title;Genre;Year;Direction'
		arq.write(cab)
	while True:
		print('\n\n\t\tWelcome!\n\n')
		options = {
            '1': new_reg,
            '2': searcha,
            '3': exit
        }
        option = input('1-Register Mov\n2-Seach\n3-exit\n>')
        if op in options.keys():
			print(options[option]())


if __name__ == '__main__':
	main()
	
