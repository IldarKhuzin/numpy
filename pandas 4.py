# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

import pandas as pd

data_authors = {
    'authors_id':[1,2,3],
    'authors_name':['Тургенев','Чехов','Островский']
}

data_book = {
    'authors_id': [1, 1, 1, 2, 2, 3, 3],
    'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    'price':[450, 300, 350, 500, 450, 370, 290]
}

authors = pd.DataFrame(data_authors)
books = pd.DataFrame(data_book)

authors_price = pd.merge(left=authors,
         right=books,
         on="authors_id")

authors_list = authors_price.authors_name.unique()

stat0 = authors_price[authors_price.authors_name == authors_list[0]]
stat1 = authors_price[authors_price.authors_name == authors_list[1]]
stat2 = authors_price[authors_price.authors_name == authors_list[2]]

stat = {
    'author_name': authors_list,
    'min_price': [min(stat0.price),min(stat1.price),min(stat2.price)],
    'max_price': [max(stat0.price),max(stat1.price),max(stat2.price)],
    'mean_price': [stat0.price.mean(),stat1.price.mean(),stat2.price.mean()]
}

author_stat = pd.DataFrame(stat)
print(author_stat)