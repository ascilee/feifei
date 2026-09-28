i = 1
q = 2
if i > q:
    print('fiefei')
print('zhangyining')
name = '张益宁'
age = 20
print(f'我的名字是： {name}, 我的年龄是：{age}')
a = 10
b = 1
b = a + b
print(b)
v = 100
def test():
    global v
    v = 200
    print(0)
test()
print(v)