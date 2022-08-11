def solution(num):
    '''
    목적: 짝수, 홀수 구분해주는 함수
    '''
    answer = ''

    # %는 파이썬에서 나머지 연산을 수행함
    if num % 2==0:
        # 숫자에서 2로 나눈 나머지가 0이면 짝수
        answer = 'Even'
    else:
        # 아닐 경우 홀수
        answer ='Odd'
    return answer

print(solution(3))
print(solution(4))