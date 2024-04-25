# [], {}
# dict: key[str,int] and 중복 안됨 - value: 아무 Type이나 넣어도됨
lecture = {
    "java": 1,
    "python": 2,
    "c": 3,
    "javascript": 4,
    "test":{
        ""
    }
}
print(lecture["java"])

coffeeShop = {
    "starbucks":[{"name":"아메리카노","kcal":150},{"name":"라떼","kcal":300}],
    "megacoffee":["아메리카노","라떼", "꿀아메리카노"],
}

coffeeShopMenu = {
    "starbucks":[{"name":"아메리카노"},{"name":"라떼"}],
    "megacoffee":[{"name":"메가리카노","price":2000},
}