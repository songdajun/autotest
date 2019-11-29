#print("你好，世界")
'''a = input("a:")
b = type(a)
print(b)'''

'''num = 123
c = type(num)
print(c)'''

'''num1 = 12345
num1 = str(num1)
print(type(num1))'''

'''a = input("你要输入的值：")
print("输出的值是：",a)'''

'''a = len("真是个小可爱！")
print(a)'''

'''a = input("请输入：")
print(len(a),a)'''
'''a = "{2} {1} {0}".format("大家好","才是真的好","噗噗")
print(a)'''

'''htuple = (1,"哈哈哈","哈哈哈","哈哈哈","哈哈哈","哈哈哈","hello",12345)
print(htuple)
print(htuple[2])
num = htuple.count("哈哈哈")
print(num)
 
a = htuple.index("hello")
print(a)
print(htuple[a]) '''

'''htuple = (1,"哈哈哈","哈哈哈","哈哈哈","哈哈哈","哈哈哈","hello",12345)
htlist = (1,"你好","hello",htuple,"橘生淮北则为枳","橘生淮南则为橘")
print(htlist[-1])'''

'''aa = ["shangke","kaixin","gaoxing","keai"]
for i in range(0,4,2):
    print(aa[i])

print("{} {}".format("haode","zhengpang"))'''
#1
'''a = int(input("a:"))
b = int(input("b:"))
print(a+b)
#2
print(type(123))
#3
print(len("dinm1234!"))
#4
print("{} {}".format("shide","wohenhao"))
#5
b = input("b:")
print(bool(b == "1"))
#6
print(type(None))
#7
a = input("a:")'''
'''
c ={"name":"dada","age":19,"address":"北京"}
print(c["age"])
print(c["age"])
print(c.get("age1"))
print(c.pop("address"))
print(c)
print(xx = c.pop(0))'''

'''age = int(input("请输入年龄："))
if age < 12:
    print("请加油！")
elif age < 22:
    print("请努力！")
elif age <30:
    print("生活保持热情！")
else:
    print("生活很美好！")'''

'''for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end = " ")
    print()'''

#0、打印99乘法表
#1、判断今天是今年的第几天。
#2、通过代码来模拟一个红绿灯的过程，其中红灯输出30次，绿灯输出35次，黄灯输出3次。
#3、模拟一个用户登录和用户注册的程序。其中账号密码都存到字典中。

'''year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = int(input("请输入天数:"))
#列出每个月份的天数
day_month = [31,28,31,30,31,30,31,31,30,31,30,31]
if year % 4 == 0 and year % 400 == 0:
    day_month[1] = 29
if month == 1:
    print(day)
else:
    n = sum(day_month[:month-1])+day
    print(n)
'''
'''log = input("登录：")
reg = input("注册：")
if log:
    a = {"username":"张三","pwd":22}
    print(a)
else:
    print(a)'''

'''choice = input("请输入您的选择：1．注册　2．登录").strip()
f = open("register.txt",'a+')
f.seek(0)
allUser = []
for user in f.readlines():
    uname = str(user).split(',')[0] #从文件中取int("username:"+uname)
    allUser.append(uname)
print("alluser:"+str(allUser))
if choice == '1':
    username = input("请输入用户名: ").strip()
    if username in allUser:
        print("该用户名已经被注册!")
    else:
        pwd = input("请输入密码:")
        pwd2 = input("再次输入密码:")
        if pwd != pwd2 or pwd.strip()=="" or pwd2.strip()=="":
            print("两次输入密码需保持一致且密码不能为空!")
        else:
            f.write(username+','+ pwd+'\n')
elif choice == '2':
    user = input("请输入用户名:")
    passwd = input("请输入密码:")
    print("登录成功")
else:
    print("输入有误!")'''


'''username = input("请输入用户名：")
pwd = int(input("请输入密码："))
aa = { }
aa.update(username=pwd)
print(aa)'''

'''for s in range(2):
    for i in range(30):
        print("红",end="")
    print(end = "\n")
    for j in range(35):
        print("绿",end="")
    print(end="\n")
    for k in range(3):
        print("黄",end="")
    print(end="\n")'''

# db = pymysql.connect(host="192.144.148.91",user="root",password="1qaz!QAZ",db="testdb")
# cursor = db.cursor()
# cursor.execute("show tables;")
# res = cursor.fetchall()
# print(res)

# import time 
# light = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print("{}距离结束时间{}秒".format(i,light[i]-j))
#             time.sleep(1)

# for i in range(10):
#     for j in range(1,(i+1)):
#         print(i,"x",j,"=",i*j,end = "  ")
#     print()

import pymysql

def chaxun(sql,dbname):
    '''
    这是数据库的查询方法
    '''
    db = pymysql.connect(host="localhost",user="root",password="123456",db=db_morniing)
    cursor = db.cursor()  # 获取游标
    cursor.execute(sql)  # 执行SQL
    res = cursor.fetchall()  # 获取所有结果
    for i in res:
        print(i)
    db.close()  # 关闭数据库连接

# def gaibian(sql):
#     '''
#     数据库的修改，新增，删除的方法
#     '''
#     db = pymysql.connect(host="localhost",user="root",password="123456",db=db_morniing")
#     cursor = db.cursor()
#     cursor.execute(sql)
#     db.commit()  # 应用/提交
#     db.close()


# query("select * from t_class;")
# query("select * from t_student;")
# query("show tables;","ljtestdb")
# query("desc t_class;")
# a = 0
# while a < 10:  
#     a = a+1
#     if a == 5:
#         break
#     print("a",a)

def query(sql):#进行封装
    '''
    这时数据库的查询方式
    '''
    import pymysql
    db = pymysql.connect(host = "localhost",user = "root",password = "123456",db = "testdb")
    cursor = db.cursor() #获取游标
    cursor.execute(sql) #执行sql
    res = cursor.fetchall() #获取所有的返回值
    for i in res:
        print(i)
    db.close() #关闭数据库连接


def commit(sql):
    '''
    数据库的修改、删除、新增的方法
    '''
    db = pymysql.connect(host = "localhost",user = "root",password = "123456",db = "testdb")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit() #提交，相当于navicat里面的对勾
    db.close()

 #调用,些不同的sql语句就可以了
query("select * from t_classs;") 
query("select * from t_student;")
query("show tables;")
query("desc t_classs ")  #desc 查询表的字段


