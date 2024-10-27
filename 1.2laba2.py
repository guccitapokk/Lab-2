from csv import reader

if __name__ == "__main__":
    author = input("Введите фамилию автора: ")
    list = []

    with open('books.csv', 'r') as csvfile:
        file = reader(csvfile, delimiter=';')
        for row in file:
            if author in row[4] and int(row[8]) <= 150:
                if row[1][1] == '#':
                    list.append(
                        f'ID:{row[0]};Название: {row[1][1:]} \n')
                else:
                    list.append(f'ID:{row[0]};Название: {row[1]} \n')

        if len(list) != 0:
            print('Книги данного автора: \n', *list)
        else:
            print('Отсутствие книг данного автора')