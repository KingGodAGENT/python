# enumerate 열거하다
fruits = [{'name':'아메리카노', 'price' : 2000},{'name':'라떼', 'price' : 3000}]
for index, item in enumerate(fruits):
    print(f"{index}. {item['name']} {item['price']}원")