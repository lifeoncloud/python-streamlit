numbers = [ 10, 20, 30, 40, 50, 60, 70, 80, 90 ]
# sublist = numbers[2:7]
# sublist = numbers[3:]
# sublist = numbers[:]

# # 인덱스2부터 인덱스7까지 2항씩 건너기
# sublist = numbers[2:7:2]

# # 뒤에서 세번째부터 뒤에서 첫번째 인덱스까지 ==> [70, 80]
# sublist = numbers[-3:-1]


# # 뒤에서 다섯번째부터 뒤에서 첫번째 인덱스까지 ==> [50, 60, 70, 80]
# sublist = numbers[-5:-1]

# # 뒤에서 다섯번째부터 뒤에서 첫번째 인덱스까지 두칸 간격으로 ==> [50, 70]
# sublist = numbers[-5:-1:2]

# 뒤에서 전체를 세는데 두칸 간격으로 있는 item을 교체하겠다 ==> [11, 20, 22, 40, 33, 60, 44, 80, 55]
numbers[::2] = [11, 22, 33, 44, 55]
print(numbers)

# # 뒤에서 다섯번째부터 뒤에서 첫번째부터 두칸 간격으로 넣는다
# sublist = numbers[-5:-1:2]
# numbers[::2] = [88, 88, 88, 88, 88]
# print(sublist)

# sublist = numbers[-5:-1:2]
# numbers[::2] = [88,88,88,88,88]

# print(numbers)
