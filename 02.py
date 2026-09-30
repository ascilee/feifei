from encodings import shift_jisx0213
from os import name
#数据类型
num = 21
pi = 3.14
s = "pyton"
flag = True
a = "张菲菲"
print(type(num))
print(type(pi))
print(type(s))
print(type(flag))
print(type(a))

x = int("123")
y = str(456)
z = float("3.14")
print(x, y, z)

#字符串
s1 = '单引号'
s2 = '双引号'
s3 = """多行
字符串"""
text = 'abcde'
print(text[0])
print(text[-1])

print(text[1:4])
print(text[::2])

print(text.upper())        #大写
print(text.lower())        #小写
print(text.replace("a", "A"))     #替换
print("a,b,c".split(","))         #分割成列表
print("hello" + "world")          #字符串拼接
print("name:{} age:{}".format("李四",22))       #格式化
print(f"名字，{name}")         #f-string （推荐）

#运算符
w = 10
q = 3
print(w + q)  #13
print(w - q)   #7
print(w * q)    #30
print(w / q)     #3.3333
print(w // q)    #3 整除
print(w % q)     #1  取余
print(w ** q)    #1000 幂运算
#赋值运算符
nup = 5
nup += 2
print(nup)
#比较运算符  >  <  >=  ==  !=
print(10 >= 5)
print(3 == 3)
print(4 != 2)
#逻辑运算符
print(1>0 and 2<3)#True
print(5>10 or 1<2)#True
print(not 1>2)    #True
#输出输入函数
name = '张益宁'
age =  20
print("姓名：", name, "年龄：", age)
print(f"姓名：{name}， 年龄：{age}")
age = input("请输入年龄：")
age= int(age)     #手动转为整数型
