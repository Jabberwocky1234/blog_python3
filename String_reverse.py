str_en = input('영어 문장을 입력하세요.\n') #문자열 입력

str_re = str() #신규 문자열형 변수 선언

for x in range(len(str_en)-1, -1, -1): #range()를 활용한 역순 인덱스 추출
    #start: 문자열 의 마지막 문자부터 end: -1에 도달하기 전 숫자인 0까지 step: -1이므로 1씩 줄인다.
    str_re += (str_en[x]) #문자열을 끝에서부터 앞으로 신규 변수에 붙이기 

print(str_re) # 위 결과 출력 

print(str_en[::-1]) #인덱스 사용법으로 역순 출력 
