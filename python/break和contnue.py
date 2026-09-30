"""
break: 直接跳出整个循环
continue:跳过本次循环，进入下一次循环
"""
for i in range(1, 10):
    if i == 5:
        break
    print(i)


for i in range(1, 10):
    if i == 5:
        continue
    print(i)
