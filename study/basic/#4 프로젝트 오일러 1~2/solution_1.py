def solution_1() -> int:
    '''
    1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하는 함수
    @param :
    @return :
        1. [정수] 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더한 수
    '''
    count = 0
    for i in range(1, 1000):
        if ((i%3)==0 or (i%5)==0):  # % 연산자로 나머지를 구함
            count += i
    return count

print(solution_1()) # 233168
