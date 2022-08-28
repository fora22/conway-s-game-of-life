'''
알고리즘
1. 전달받은 폰켓몬 리스트에서 가져갈 수 있는 최대 폰켓몬 수를 계산 N/2
2. 전달받은 폰켓몬 리스트에서 고유한 종류의 폰켓몬이 몇마리 있는지 계산
3. 최대 폰켓몬 수 < 고유한 종 수 -> 최대 폰켓몬 수를 반환
4. 최대 폰켓몬 수 > 고유한 종 수 -> 고유한 종 수를 반환
'''

import math


def solution(nums):
    '''
    가질 수 있는 폰켓몬 종류 수의 최댓값을 계산해주는 함수
    '''
    type = len(set(nums)) # set()함수로 중복되지 않는 폰켓몬의 종류를 구하고, len()함수로 그 개수를 구한다.
    take_ponketmon = math.floor(len(nums)/2) # (nums의 원소 개수)/2 -> 정수로
    if take_ponketmon > type: # (nums의 원소 개수)/2 > len(set(nums))이면 중복되지 않는 폰켓몬 종류의 수를 반환한다.
        return type
    else: # (nums의 원소 개수)/2 <= len(set(nums))면 골라야 하는 폰켓몬의 수(len(nums)/2)를 반환한다.
        return take_ponketmon

def solution_2(nums: list) -> int:
    '''
    solution 의 또 다른 풀이 by forapaeng1021

    문제설명:
        총 N마리가 주어지고 -> nums 의 길이 -> 항상 짝수
        
        가져갈 수 있는 폰켓몬은 N/2
    
    해결방법:
        가져갈 수 있는 폰켓몬의 수 중에서 
        가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아야 함
    '''
    N = len(nums)
    take_ponketmons = int(N / 2) # Math.floor 버림 처리 -> int 처리하는게 이해가 직관적
    type_of_ponketmons = len(set(nums))   # set() 함수로 중복되지 않는 폰켓몬 종류 수를 구함

    # 둘 중 최솟값을 return
    return min(take_ponketmons, type_of_ponketmons)


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))