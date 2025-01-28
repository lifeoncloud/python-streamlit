STUDENTS = 5
lst = []
count = 0

for i in range(STUDENTS):
    ## 성적 데이터를 정수 타입으로만 받음
    value = int(input("성적을 입력하세요."))
    lst.append(value)

print(f"성적평균 = {sum(lst)/len(lst)}")
print(f"최대 점수 = {max(lst)}")
print(f"최소 점수 = {min(lst)}")

for score in lst:
    # score가 80 이상일 때만 count를 하나씩 +1 한다
    if score >= 80:
        count += 1

print(f"80점 이상은 = {count}명입니다.")
