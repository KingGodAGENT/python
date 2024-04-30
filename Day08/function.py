# 함수: input[int, str, [], None] -> output
# 마술상자: [100 -> 500, 200 -> 1000, 300 -> x]
# f(x): len(x), str(x), input(x), print(x) 등
# count("p")

'''
def koreaIt(i):
    return i + "코리아아이티"
a = koreaIt("인천점")
print(a)

# count("p")
def koreaIt(i):
    return i + "코리아아이티"

def add(x,y):
    return x+y
a = add(1,2)
print(a)
'''

# 어떤 단어를 넣었을 때, 그 단어가 5글자 이상이면
# 글자가 길어요!, 아니면 글자가 짧아요!

'''
def isWordLong(i):
    if len(i) >= 5:
        return "글자가 길어요!"
    else:
        return "글자가 짧아요!"
'''

# 함수: input -> [로직] -> output

# abc(3,'😜')
# ['😜', '😜', '😜']

'''
def makeEmojiList(x,y):
    return [y for x in range(x)]
'''

# 이모지 단축키 : 윈도우키 + .

# ❤ 💋 ✌ 😜 😍
# ❤ -> 💋
# 💋 -> ✌
# ✌ -> 😜
# 😜 -> 😍


'''
def changeEmoji(x):
    if x == '❤':
        return '💋'
    elif x == '💋':
        return '✌'
    elif x == '✌':
        return '😜'
    elif x == '😜':
        return '😍'
    else:
        return "에러"
print(changeEmoji('💋'))
'''

'''
def changeEmoji(x):
    dictChange = {
        '❤': '💋',
        '💋': '✌',
        '✌': '😜',
        '😜': '😍',
    }
    return dictChange[x]
print(changeEmoji('😜'))
'''