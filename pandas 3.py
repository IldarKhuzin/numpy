# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

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

top = authors_price.sort_values(by='price', ascending=False)

top_5 = top.head(5)
print(top_5)
