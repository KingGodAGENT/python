# 게임 몬스터 프로그램

def killingMonster(monster,event):
    print(f"{monster}를 처치했습니다!")
    event()

def getGold():
    print("골드 획득!")

def getFood():
    print("음식 획득!")

killingMonster("슬라임", getGold)
killingMonster("늑대", getFood)