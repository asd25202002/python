def sum_num():
    sum = 0
    n,m = eval(input("請輸入2個數字(以逗號隔開): "))
    if n > m: n,m = m,n
    for i in range(n,m+1):
        sum += i
    print(sum)
def euler():
    e = 1
    for i in range(1,101):
        temp = 1
        for j in range(1,i+1):
            temp *= j
        e += 1/temp
        if i % 10 == 0:
            print(e)
def Prime():
    ans = []
    for i in range(1,21):
        for j in range(2,i):
            if i % j == 0 and (i != 1 or i != 2):
                break
        else:
            ans.append(i)
    for s in ans:
        print(s,end=" ")
def gcd():
    n,m = eval(input("請輸入2個數字(以逗號隔開): "))
    if n > m: n,m = m,n
    for i in range(2,n+1):
        if n % i == 0 and m % i == 0:
            ans = i
    print("{} 與 {} 的最大公因數為 {}".format(n,m,ans))