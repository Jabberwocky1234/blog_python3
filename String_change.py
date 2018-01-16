str_en = input('영어 대소문자로 이루어진 문장을 입력하세요.\n')

print('모두 대문자로 출력\n' + str_en.upper())

print('모두 소문자로 출력\n' + str_en.lower())

new_str = str()

for ch in str_en:
    if ch.islower():
        new_str += ch.upper()
    else:
        new_str += ch.lower()
        
print('대소문자 바꿔서 출력(for문)\n' + new_str)

print('대소문자 바꿔서 출력(문자열 내장 메소드)\n' + str_en.swapcase())
