# 加法
# a=int(input("請輸入第一個數字："))
# b=int(input("請輸入第二個數字："))
# c=a+b
# print(f'{a}+{b}={c}')

# 算BMI
height=float(input("輸入你的身高(m):"))
weight=float(input("輸入你的體重(kg):"))

bmi=weight/height/height

if bmi>24:
    print(f"bmi是{bmi:.1f},過重")
if 18<bmi<24:
    print(f"bmi是{bmi:.1f},適中")
if bmi<18:
    print(f"bmi是{bmi:.1f},過輕")
