# 1. 뉴스 기사를 스크랩해오고, 유저가 입력한 단어를 뉴스기사에서 그 해당 단어를 모두 대문자로 보여주기

# news = "saudi arabia claims that women now make up around 35% of the country's workforce."
# a = input("찾을 문자를 입력하세요:")
# b = news.replace(a,a.upper())
# print(b)

# 2. 영어 기사를 스크랩 해오고, 단어 사이에 😜 넣고 출력하기

news = "saudi arabia claims that women now make up around 35% of the country's workforce."
a = news.split(" ")
b = "😜".join(a)
print(b)


