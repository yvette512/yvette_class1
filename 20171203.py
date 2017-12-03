print("hello world")

#encoding=utf-8

# string1="happy birthday to you ，my dear  "
#
# print(len(string1))
# print(string1[1:9])
# print(string1.capitalize())
# print(string1.replace(",","!"))
# print(string1.rstrip())
# print(len(string1.rstrip()))
# print(string1.upper())
# print(string1.split())
#
# list1=['beijing','nanjing','shuanghai','guangzhou']
# print(' '.join(list1))


#有⼀个列表：  l1 = ['b','c','d','b','c','a','a']
# 1.统计'C'重复的元素个
# 2. 去重
# 3. 按照顺序输出
# 4. 反转
# 5. 将列表转化为字

ll=['b','c','d','b','c','a','a']
print("c出现的次数：",ll.count('c'))
ll.sort(reverse=True)
print("ll从大到小排序",ll)
ll.reverse()
print("反转",ll)
print("将列表转换成字符串:",",".join(ll))
