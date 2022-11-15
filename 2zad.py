a = int(input())
k = int(input())
b = ""
a_1 = a
k_1 = k
while a > 0:
    b = str(a % 2) + b
    a = a // 2
vivod = int(b)
for i in range(k):
    if vivod % 10 == 0:
        vivod = vivod/10
    if vivod % 10 == 1:
        vivod = vivod//10 +1

vivod = int(vivod)
b = 0
s = 0
dlina = len(str(vivod))
for k in range(0,dlina):
    b = (vivod%10)*(2**(k))
    s += b
    vivod= vivod//10
print(a_1,":","(","2","^",k_1,")","=",s)
