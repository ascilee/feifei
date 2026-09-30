lst = [10, 20, 30, "python"]
print(lst[0])
print(lst[-1])


#增加元素
lst.append(40)         #末尾追加
lst.insert(1, 15)      #指定位置插入
lst.extend([50, 60])   #末尾追加多个元素

#删除元素
lst.pop()              #删除最后一个， 返回值
lst.pop(0)             #删除索引0
lst.remove(20)         #删除指定元素第一个匹配项



#改
lst[0] = 99


#查
print(20 in lst)      #判断是否存在

#常用
print(len(lst))        #长度
lst.sort()           
"""
排序    Python 无法拿字符串和数字比较大小  
方案 1：列表只保留同一种类型
方案 2：全部转为字符串再排序
lst = [99, 30, 'python', 40, 50]
lst.sort(key=str)  # 全部当成字符串来比较
print(lst)
"""
lst.reverse()          #反转
