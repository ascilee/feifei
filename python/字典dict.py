#键值对 key:value，key 不可重复、必须不可变类型
dic = {'name': '王五', 'age' : 20}
print(dic["name"])
print(dic.get("age"))


#增改
dic["gender"] = "男"
dic["age"] = 21


#删
dic.pop("gender")
#dic.pop("name")


#遍历
for k in dic:
    print(k, dic[k])

for k,v in dic.items():
    print(k, v)


print(dic.keys())
print(dic.values())
