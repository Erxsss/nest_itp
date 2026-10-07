n = int(input("enter sec="))
hour = n//3600
min = (n-hour*3600)//60
sec = n-hour*3600-min*60

print(hour , min , sec)

money = int(input("amount="))
twent = money//20000
ten = (money-twent*20000)//10000
fiv = (money-twent*20000-ten*10000)//5000
one = money-twent*20000-ten*10000-fiv*5000
print(twent,ten,fiv,one)

num = input("enter=")
revNum= num.reverse()
print(revNum)

num =int(input("enter="))
num1 = num%10
num2 = num//10%10
num3 = num//100%10
num4 = num//1000%10
print(num1*num1+num2*num2+num3*num3+num4*num4)

day = int(input("day"))
hour = int(input("hour"))
min = int(input("min"))
sec = int(input("day"))
print(day*3600*24+hour*3600+min*60+sec)

une = int(input("une"))
hymd = int(input("hymd"))
print(une-une*hymd//100)