# class MyError(Exception):
#     def __init__(self,text="MyError"):
#         self.text = text
#
# def inputFromUser():
#     b = int(input())
#     if b == 0:
#         raise MyError()
#     return b
#
# try:
#     a = inputFromUser()
# except Exception as e:
#     print(e)
#     a = 1
# if a%2 == 0:
#         print(10/a)
# else:
#     print(10*a)
#
#
# def somefunction():
#     er = False
#     try:
#         a = inputFromUser()
#         if a % 2 == 0:
#             print(10 / a)
#         else:
#             print(10 * a)
#     except:
#         er=True
#     finally:
#         return er
#
#
#



# def inputFromUser():
#     b = int(input())
#     if b == 0:
#         raise MyError("Ошибка")
#     return b
#
# def somefunction():
#     er = True
#     try:
#         a = inputFromUser()
#         if a % 2 == 0:
#             print(10 / a)
#         else:
#             print(10 * a)
#     except:
#         er= False
#     finally:
#         return er
#
# assert(somefunction())
#



# import random
# def getText():
#     if random.randint(0,1) == 1:
#         return "text"*2
#     else:
#         return 2
#
# file = open('test.txt',"w+",encoding = "utf-8")
# try:
#     file.write(getText())
#     print(file.read())
# except TypeError:
#     file.write(str(getText()))
#     print(file.read())
# except:
#     print("Непредвиденная ошибка")
# finally:
#     file.close()


# import random
# try:
#     a = int(input())
#     print(a/random.randint(1,10))
# except:
#     print("ошибка")
# finally:
#     print("ошибка2")
#
#
# import random
# try:
#     a = int(input())
#     out = a/random.randint(1,10)
# except:
#     out = "ошибка"
# finally:
#     print(out)
#

try:
    one = int(input())
    two = int(input())
    out = lambda a,b: a/b
    print(out(one,two))
except:
    print("ошибка")
