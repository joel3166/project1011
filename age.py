from datetime import datetime

def calculate_age(birthdate):
    # 현재 날짜 가져오기
    current_date = datetime.now()

    # 생년월일을 파싱
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')

    # 만 나이 계산
    age = current_date.year - birth_date.year

    # 현재 날짜가 생년월일을 지났는지 확인
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1

    return age

# 사용자로부터 생년월일 입력 받기
birthdate = input("생년월일(예: 2000-01-01)을 입력하세용: ")

# 만 나이 계산
age = calculate_age(birthdate)

# 결과 출력
print(f"만 나이: {age}세 입니당")
