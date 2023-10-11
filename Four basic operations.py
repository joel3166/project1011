# 두 숫자를 입력받습니다.
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 덧셈
addition = num1 + num2
print(f"덧셈 결과: {addition}")

# 뺄셈
if num1 > num2:
    subtraction = num1 - num2
    print(f"뺄셈 결과: {subtraction}")
else:
    subtraction = num2 - num1
    print(f"뺄셈 결과: {subtraction}")
    
# 곱셈
multiplication = num1 * num2
print(f"곱셈 결과: {multiplication}")

# 나눗셈
if num2 == 0:
    print("0으로 나눌 수 없습니다.")
else:
    division = num1 / num2
    print(f"나눗셈 결과: {division}")
