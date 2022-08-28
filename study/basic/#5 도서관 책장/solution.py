import os

dir_path = os.path.abspath(os.path.dirname('./'))
input_file_name = 'input.txt'

def get_book_data() -> list:
    '''
        input.txt에서 book 데이터를 가져오는 함수
        @param
        @return
            1. book_data [2차원 리스트] book 데이터를 2차원 리스트로 표현
    '''
    try:
        books = open(f'{dir_path}\\{input_file_name}', 'r')
    except Exception as error:
        print("file 을 읽는 중 에러가 발생했습니다!")
        print(error)

    book_data = []
    while True:
        book_info = books.readline()    # 한 줄 읽고
        if not book_info:
            # 다 읽으면 break -> while stop
            break
        book_info_list = book_info.split()
        book_data.append(book_info_list)

    return book_data

def solution(word):
    '''
    도서관 책장 안에 5권의 책이 있습니다.
    사용자에게 검색어를 입력받고, 검색어를 통한 도서 검색이 가능한 함수를 작성해주세요.
    '''
    book_data = get_book_data()
    print(book_data)    # [ [..], [..], ... ] 형태의 2차원 리스트

    # 도서 검색 기능을 정의


search_word = input("검색어를 입력해주세요: ")
solution(search_word)