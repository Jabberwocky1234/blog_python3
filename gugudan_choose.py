n = int(input('구구단 몇 단을 출력할까요? 숫자를 입력하세요: '))
while 1>n or 9<n:
    n = int(input('구구단은 1~9단까지만 출력 가능합니다. 맞는 숫자를 다시 입력하세요: '))

for m in range(1, 10):
    print(n, 'x', m, '=', n*m)


