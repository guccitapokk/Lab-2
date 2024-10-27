from csv import reader

count = 0
with open('books.csv', 'r') as csvfile:
    file = reader(csvfile, delimiter=';')
    for row in file:
        if len(row[1]) > 30:
            count += 1

print(f"Книги, где в названии присутствует > 30 символов: {count}")