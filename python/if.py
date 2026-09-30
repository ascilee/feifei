score = int (input("输入分数："))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("及格")
else:
    print("不及格")



#三元表达式
age = int(input("请输入年龄："))
res = "成年" if age >=18 else "未成年"
print(res)