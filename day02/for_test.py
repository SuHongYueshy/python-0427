for i in range(0, 10):  #
    print(i)

fruits = ['apple', 'banana', 'orange', 'watermelon']  # list 列表
# fruits = []  # list 列表
for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        break
else:  # 循环正常结束后的处理：没有 break
    print('else...')

for fruit in fruits:
    print(fruit)
    if fruit == 'watermelon':
        # proceed...
        print('found watermelon.')
        break
# else:  # 循环正常结束后的处理：没有 break
#     print('not found watermelon.')

