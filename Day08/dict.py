# (기본 타입) a = 1, b = 3.14, c = True, d = "hello"
# e = [], f = {} set or dict

# key

person = {
    'name' : "엄준식",
    'age' : 23,
    'town' : "동탄시",
    'coffeeList' : ["아메리카노", "라떼", "민트"],
    'academy' : {
        "first": "java",
        "second": "c-language",
        "third": "python",
    },
}

print(f"이름:{person["name"]} 동네:{person["town"]} 좋아하는 커피 3번째:{person["coffeeList"][2]} 학원 세번째 수업:{person['academy']['third']}")

# 데이터 생성
person["gender"] = "male" # key , value 데이터 만들기

# 데이터 삭제
del person["town"]
print(person)

print(person.keys()) # key
print(person.values()) # value
print(person.items()) # k , v 모두









