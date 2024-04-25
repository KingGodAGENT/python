# data-type: int, str, float, bool, list
# set (집합)
# 중복 허용 안되는 타입

a = {1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8}
burgerking = {"새우와퍼","불고기와퍼","치즈와퍼","스테이크와퍼"}
momstouch = {"새우와퍼", "치즈와퍼", "싸이버거", "불고기버거"}
x = burgerking.intersection(momstouch)
print(x)

# 합집합 (|)
union = burgerking | momstouch

# 교집합 (&)
intersection = burgerking & momstouch # 새로운 문법
intersection1 = burgerking.intersection(momstouch) # 옛날 문법


# 차집합 (-)
difference = burgerking - momstouch

print(union)
print(intersection)
print(difference)

# 추가
burgerking.add("와퍼주니어")

# 삭제
burgerking.remove() # 옛날 문법 (없는 요소를 쓰면 에러뜸)
burgerking.discard() # 요즘 문법 (없는 요소를 써도 실행됨

# 전체 삭제
burgerking.clear()

# set() (중요!)
result = set([1,2,3,1,2,3])
print(list(result))

news = """Koreans’ stereotypes about gender roles regress compared to 3 years ago"""
wordList = news.split()
noDuplicationWords = list(set(wordList))
noDuplicationWords.sort()
print(noDuplicationWords)







