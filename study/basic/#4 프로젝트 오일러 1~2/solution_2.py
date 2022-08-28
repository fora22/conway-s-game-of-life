def solution_2() -> int:
    '''
    피보나치(Fibonacci) 수열의 각 항은 바로 앞의 항 두 개를 더한 것입니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더하는 함수
    @param :
    @return :
        1. [정수] 4백만 이하의 짝수 값을 갖는 모든 피보나치 항을 더한 수
    '''
    number_1 = 1    # first_number
    number_2 = 2    # second_number
    count = 0
    while (number_1 <= 4000000):
        number_1, number_2 = number_2, number_1 + number_2
        if ((number_1%2)==0):
            count += number_1
    return count

print(solution_2()) # 4613732