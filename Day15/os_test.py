import os
import datetime
from review import yearToZodiac

# 바탕화면 경로따기
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# 바탕화면 경로와 폴더이름 합치기
folder_path = os.path.join(desktop_path,'폴더이름')

# 폴더 만들기
os.mkdir(folder_path)

# 오늘 날짜 가져오기
start_date = datetime.date.today()

for i in range(365):
    date_folder = start_date + datetime.timedelta(days=i)
    path = os.path.join(folder_path, date_folder.strftime("%Y-%m-%d"))
    os.mkdir(path)

# for i in range(365):
#     date_folder = start_date + datetime.timedelta(days=i)
#     year_zodiac = yearToZodiac(int(date_folder.strftime('%Y')))
#     folder_name = f"{year_zodiac}띠의 해_{date_folder.strftime('%mm_%d_%A')}"
#     path = os.path.join(folder_path,folder_name)
#     os.mkdir(path)














