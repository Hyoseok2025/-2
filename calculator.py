def calculator():
    print("간단한 계산기 프로그램입니다.")
    print("1. 덧셈")
    print("2. 뺄셈")
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 종료")
    
    while True:
        choice = input("\n원하는 연산을 선택하세요 (1-5): ")
        
        if choice == '5':
            print("계산기를 종료합니다.")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("잘못된 선택입니다. 1-5 사이의 숫자를 선택해주세요.")
            continue
            
        try:
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
            
            if choice == '1':
                result = num1 + num2
                print(f"결과: {num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"결과: {num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"결과: {num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("0으로 나눌 수 없습니다!")
                    continue
                result = num1 / num2
                print(f"결과: {num1} / {num2} = {result}")
                
        except ValueError:
            print("올바른 숫자를 입력해주세요.")

if __name__ == "__main__":
    calculator()