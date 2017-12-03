#encoding=utf-8

# sting1=("23","34","334","0987")
# #字典，是按照KEY值来访问的
# prince={"haode":"yige","hua":[1,2,4,5,6,7,8,9,83333],"jjhh":99}
#
# print(prince["haode"])
# print(prince["hua"])
# print(sting1[0])

# #求整
# print(3/5)
# print(5/3)
#
# #求余
# print(7%3)

# ==
#
# #逻辑运算符，
# string1=True
# string2=False
# string3=True
# if string1==True and string2==True:
#     print("OK")
# else:
#     print("Cancle")
#
# if string2==True and string3==True:
#     print("你是对的")
# else:
#     print("you are loser")

#
# #
# # number1=1
# # number2=344
# # number3=4444
# # number3+=number1 #等价number3=number3+number1
# # print(number3)
#
# # string="my name is yevtte"
# # if "my" in string:
# #     print("Yes")
# # else:
# #     print("NO")
# # if "is" not in string:
# #     print("YYYYY")
# # else:
# #     print("NNNNN")
#
# mytype=none
def hello():
    print("hhhhh")
hello()

# string 类型的值，若要算平均值需要转换成int或float类型，
# # 才能计算，但有的版本的python会自动把string转换成数值类型
# string1=input("请输入一个成绩：")
# print(type(string1))
# string2=input("请再次输入一个成绩：")
# print(type(string2))
# print((string1+string2)/2)
# print(type((string1+string2)/2))

#
# #字符串切片和连接，截取是前开后闭的
# string2="hello,world"
# print(len(string2))#打印字符串长度
# #取第几个
# print(string2[10])
# print(string2[-1])
# #分割
# print(string2[1:-1])#截取1~-1
# print(string2[:5])#截取0~5
# print(string2[1:])#截取1~
# print(string2[:])#截取全部的
# print(string2[0:])#截取全部
# print(string2[1:5])#截取1~5
# #步长截取
# print(string2[::2])#每隔两个
# print(string2[::-2])#倒序，每隔两个
#
# #拼接
# website="www"+"."+"baidu"+"."+"com"
# print(website)

#format 类型转换
# my_name="Yvette"
# my_aa=76
# print("my name is %s，my aa is %s" %(my_name,my_aa)) # %s 是字符串，%d是int整型
# print("my name is {},my age is {}".format(my_name,my_aa))
# print("my name is {0},my age is {1}".format(my_name,my_aa))
# print("my name is {name},my age is {age}".format(name=my_name,age=my_aa))



#
# #字符串的内建函数
# inital_string="welcome to china   "
# space_string=""
# # print inital_string.capitalize()
# # if inital_string.endswith(""):#以空格结尾
# #     print("OK")
# # else:
# #     print("NO!!!!!")
# # if inital_string.find("t"):#找t所在的长度
# #     print inital_string.find("t")
# # print  inital_string.index('e')
# if space_string.isspace():
#     print ("It is space")
# else:
#     print( "It not space")
#
#
# if inital_string.islower():
#     print inital_string.upper()
#
# if inital_string.isupper():
#     print inital_string.lower()
#     print ("这是大写")
# else:
#     print("这不是大写")
#

# inital_string="Welcome to china"
# score_list=["90",'89','24','87','100']
# scores=','.join(score_list)
# # print type(scores)
# # print scores
# #
# # print len(inital_string)
# # print len(score_list)
# yy=inital_string.lstrip()
# print yy
# print len(inital_string.lstrip())
#
# print inital_string.rstrip()
# print len(inital_string.rstrip())
#

#
# inital_string="HELLO EVERYONE"
# inital="we are the best"
# if inital_string.upper():
#     print inital_string.lower()
#
# else:print ("不是大写")
#
# if inital_string.startswith("H"):
#     print inital_string.replace("H","P")
#     print len(inital_string.replace("h","P"))
#     print inital_string.replace("H","p").strip()
#     print len(inital_string.replace("H","P").strip())
#
ll=['b','c','d','b','c','a','a']
print("c出现的次数：",ll.count('c'))
ll.sort(reverse=True)
print("ll从大到小排序",ll)
ll.reverse()
print("反转",ll)
print("将列表转换成字符串:",",".join(ll))

# print type(inital)
# print inital.split(" ")
# print type(inital.split(" "))

print("heyyh")
inital_string="HELLO EVERYONE"

my_list=['china','japan','USA']
my_string=" ".join(my_list)
print(my_string)
print(type(my_string))
print(type(my_list))
print("git github")