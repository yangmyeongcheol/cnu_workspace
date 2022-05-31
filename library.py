#####################################
# 프로그래: 도서관 관리 프로그램
# 작성자: 양명철
# 작성일자: 2022.5.10
# - 메인화면 출력
#####################################

import sys
import service.BookService as bookService
import service.MemberService as memberService

while True:
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: CNU LIBRARY')
    print('::  - ADMIN Mode')
    print('::  - ver1.0')
    print('::  - made by Ynag')
    print('::  - last update 2022.05.10')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('::  1.도서 목록')
    print('::  2.도서 검색')
    print('::  3.도서 대출')
    print('::  4.도서 반납')
    print('::  5. 회원 목록')
    print('::  6.회원 검색')
    print('::  7.프로그램 종료')
    print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

    while True:
        print(':: 실행하고 싶은 서비스의 번호를 입력하세요.')
        select_num = int(input('>> 입력: '))
        if 1 <= select_num <= 7:
            break
        else:
            print('#Waring: 올바른 번호를 입력하세요.')

    if select_num == 1:  # 도서 목록
        bookService.get_books()
    elif select_num == 2:  # 도서 검색
        bookService.search_books()
    elif select_num == 3:  # 도서 대출
        pass
    elif select_num == 4:  # 도서 반납
        pass
    elif select_num == 5:  # 회원 목록
        memberService.get_members()
    elif select_num == 6:  # 회원 검색
        pass
    elif select_num == 7:  # 프로그램 종료
        print('Exit Program, Bye Bye :)')
        sys.exit()
