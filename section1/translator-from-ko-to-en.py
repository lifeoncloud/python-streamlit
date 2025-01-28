import googletrans

translator = googletrans.Translator()

input_korean = input("한국어를 입력하세요 : ")
translated = translator.translate(input_korean, src="ko", dest="en").text

print(f"한국어 입력 값 : {input_korean}")
print(f"영어 번역 결과 : {translated}")
