names = ["조정원", "홍길동", "김민석", "김지영", "이희영"]

# # 일반 리스트 출력하기
# print(names[0])
# print(names[1])
# print(names[2])

# for name in names : 
#     print(name)

# for i in range(len(names)) : 
#     print(f"인덱스: {i+1}의 이름은: {names[i]}")

# enumrate는 names의 인덱스인 i와 value인 name을 같이 가져온다
print("현재 인덱스와 이름을 알려드립니다.========")
for i, name in enumerate(names): 
    print(f"인덱스{i+1}의 이름은 {name}")



# 사용자 리스트 출력
name_append = input("추가할 이름은: ")
names.append(name_append)
for i in range(len(names)):
    print(f"인덱스{i+1}의 이름은 {names[i]}")
