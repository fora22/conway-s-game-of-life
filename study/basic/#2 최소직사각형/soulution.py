def solution(sizes):
    '''
    목적: 최소 직사각형의 넓이를 계산해주는 함수
    '''
    answer = 0
    # 리스트(list) 안에 있는 아이템(item) 반복
    width = []
    height = []
    for _, item in enumerate(sizes):
        # item에서 0번째는 w, 1번째는 h
        # width, height : 너비, 높이
        w = item[0] # width
        h = item[1] # height
        
        # w랑 h비교 -> h 가 클 경우, w랑 h랑 교체
        if w < h:
            temp = h
            h = w
            w = temp
        
        width.append(w)
        height.append(h)

    # 마지막으로 w 중에 최댓값, h 중에 최댓값 구하기
    max_w = max(width)
    max_h = max(height)

    # return w 최댓값 * h 최댓값 
    answer = max_w * max_h
    return answer

print(solution([[60,50],[30,70],[60,30],[80,40]]))
print(solution([[10,7],[12,3],[8,15],[14,7],[5,15]]))
print(solution([[14,4],[19,6],[6,16],[18,7],[7,11]]))