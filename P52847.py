from easyinput import read

num1, num2, num3 = read(int, int, int)

if num1<num2 and num2<num3:
    print(num3)

elif num1<num3 and num3<num2:
    print(num2)
elif num2<num3 and num3<num1:
    print(num1)