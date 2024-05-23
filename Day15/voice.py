from gtts import gTTS

text = "오늘이 지나면 내일은 금요일"
a = gTTS(text, lang='ko')
a.save("result.mp3")