#使用 split
integers = input("請輸入數字: ")
integer = integers.split(' ') #以空格隔開
num1,num2,num3,num4 = integer[0],integer[1],integer[2],integer[3] #以陣列形式帶入
print("第1個值: {}\n第2個值: {}\n第3個值: {}\n第4個值: {}\n".format(num1,num2,num3,num4))


#使用 split
integers = input("請輸入數字: ")
integer = integers.split(' ') #以空格隔開
num1,num2,num3,num4 = integer
print("第1個值: {}\n第2個值: {}\n第3個值: {}\n第4個值: {}\n".format(num1,num2,num3,num4))


#使用 eval
integers = eval(input("請輸入數字: "))
num1,num2,num3,num4 = integers
print("第1個值: {}\n第2個值: {}\n第3個值: {}\n第4個值: {}\n".format(num1,num2,num3,num4))